<template>
	<view class="pics">
		<scroll-view class="left" scroll-y>
			<view 
			@click="leftClick(index,item.id)"
			:class="index===active?'active':''" 
			v-for="(item,index) in cases" 
			:key="item.id">
			{{item.title}}</view>
		</scroll-view>
		<scroll-view class="right" scroll-y>
			<view @click="preview(item.image)" class="item" v-for="item in secondData" :key="item.id">
				<image :src="item.image"></image>
				<text>{{
					item.title
				}}</text>
			</view>
			<view v-if="cases.length===0">暂无数据</view>
		</scroll-view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				cases:[],
				active:0,
				secondData:[]
			}
		},
		methods:{
			async getPicsCate(){
				const res=await this.$myRequest({
					url:"/api/lunbo/getcategory/"
				})
				// console.log(res.data.message)
				this.cases=res.data.message
				this.leftClick(0,this.cases[0].id)
			},
			async leftClick(index,id){
				this.active=index
				 const res=await this.$myRequest({
					url:"/api/lunbo/category/"+id
				})
				this.secondData=res.data.message
			},
			preview(current){
				const urls=this.secondData.map(item=>{
					return item.image
				})
				uni.previewImage({
					urls,
					current
				})
			}
		},
		onLoad() {
			this.getPicsCate()
		}
	}
</script>

<style lang="scss">
	page{
		height: 100%;
	}
	.pics{
		height: 100%;
		display: flex;
		.left{
			width: 200rpx;
			height: 100%;
			border-right: 1px solid #eee;
			view{
				height: 60px;
				line-height: 60px;
				font-size: 30rpx;
				color: #333333;
				text-align: center;
				border-top: 1px solid #eee;
			}
			.active{
				color: #FFFFFF;
				background-color: $shop-color;
			}
		}
		.right{
			height: 100%;
			width: 520rpx;
			margin: 0 auto;
			.item{
				image{
					width: 520rpx;
					height: 400rpx;
					border-radius: 5;	
					border-top: 1px solid #eee;
				}
				text{
					font-size: 30rpx;
					line-height: 60rpx;
					background-color: #EECFA1;
				}
			}
		}
	}
</style>
