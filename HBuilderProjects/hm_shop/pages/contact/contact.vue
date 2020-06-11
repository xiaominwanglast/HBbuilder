<template>
	<view class="contact">
		<image src="http://www.itcast.cn/2018czydz/images/gywmban.jpg"></image>
		<view class="info">
			<view @click="makephone">联系电话：17621145335[点击拨打]</view>
			<view>联系地址：上海市浦东新区康桥镇康佳路39弄向里走应该能走到</text></view>
		</view>
		<map class="map" :scale="scale" :latitude="latitude" :longitude="longitude" :markers="markers"></map>
	</view>
</template>

	
<script>
	export default{ 
		data(){
			return{
				latitude:31.132753,
				longitude:121.602453,
				scale:16,
				markers:[
					{
						latitude:31.132753,
						longitude:121.602453,
						iconPath:"../../static/icon/location.png",
						width:20,
						heigh:30
					}
				]
			}
		},
		methods:{
			makephone(){
				uni.makePhoneCall({
					phoneNumber:"17621145335"
				})
			}
		}
	}
</script>

<style lang="scss">
	.contact{
		image{
			width: 100%;
			height: 300rpx;
		}
		.info{
			padding: 10rpx 20rpx;
			font-size: 30rpx;
			view{
				line-height: 80rpx;
				border-bottom: 1px solid #eee;
			}
		}
		.map{
			width: 100%;
			height: 500rpx;
		}
	}
</style>
