<template>
	<view class="tuijian_content">
		<view class="tuijian_item" v-for="(item,index) in moreData" :key="index">
			<image style="height: 60px;" :src="src"></image>
			<view class="tuijian_content_text">
				<text>{{item.name}}</text>
				<text>详细地址:{{item.address}}</text>
				<text>#距离{{item.distance}}&nbsp;&nbsp;步行预计{{item.duration}}&nbsp;&nbsp;{{item.telephone!=''?"电话："+item.telephone.split(',')[0]:''}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				lat:0,
				lng:0,
				type:"",
				moreData:[],
				src:"../../static/images/wangba.jpeg"
			}
		},
		methods: {
			async getMore(lat,lng,type){
				const res=await this.$myRequest({
					url:"api/map/getmore/?lat="+lat.toString()+"&lng="+lng.toString()+"&type="+type
				})
				this.moreData=res.data.message.slice(0,10)
				if(type=="shop"){
					this.src="../../static/images/chaoshi.jpeg"
				}
			}
		},
		onLoad: function (option) { 
			this.lat=option.lat
			this.lng=option.lng
			this.type=option.type
			this.getMore(this.lat,this.lng,this.type)
		}
	}
</script>

<style lang="scss" scoped>
	.tuijian_content{
		font-size: 30px;
		display: flex;
		flex-wrap: wrap;
		// justify-content: space-between;
		background-color: #FFFAFA;
		.tuijian_item{
			border: 1px solid #C0C0C0;
			width: 100%;
			margin: 0 0;	
			display: flex;
			image{
				heigh:100%;
				width:80px;
			}
			.tuijian_content_text{
				font-size: 35rpx;
				display: flex;
				width: 100%;
				flex-direction:column;
				text{
					color: #0D0D0D;
					margin-top: 5px;
					font-size: 35rpx;
				}
				text:nth-child(2){
					color: #0D0D0D;
					font-size: 25rpx;
				},
				text:nth-child(3){
					color: #FF7256;
					font-size: 25rpx;
				}
			}
		}
	}
</style>
