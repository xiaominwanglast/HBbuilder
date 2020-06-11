<template>
	<view class="home">
		<swiper indicator-dots circular>
			<swiper-item v-for="item in swiperList" :key="item.id">
				<image :src="item.image"></image>
			</swiper-item>
		</swiper>
		<view class="nav">
			<view class="nav_item" v-for="(item,index) in navs" :key="index" @click="navitemClick(item.page)">
				<view :class="item.icon"></view>
				<text>{{item.title}}</text>
			</view>
		</view>
		<view class="hot_goods"> 
			<view class="tit">推荐商品</view>
			<goods-list @goodsItemClick="goDetail" :goods="goods"></goods-list>
		</view>
	</view>
</template>

<script>
	import goodslist from "../../components/goods-list/goods-list.vue"
	export default {
		data() {
			return {
				swiperList:[],
				goods:[],
				navs:[
					{
						title:"视频资源",
						icon:"iconfont icon-bofang",
						page:"/pages/videos/videos"
					},
					{
						title:"黑马超市",
						icon:"iconfont icon-fuwuchaoshi",
						page:"/pages/goods/goods"
					},					{
						title:"联系我们",
						icon:"iconfont icon-CONTACT",
						page:"/pages/contact/contact"
					},					{
						title:"社区图片",
						icon:"iconfont icon-tupian",
						page:"/pages/pics/pics"
					}
				]
			}
		},
		onLoad() {
			this.getSwiper()
			this.getGoods()
		},
		components:{
			"goods-list":goodslist
		},
		methods: {
			async getSwiper(){
				const res =await this.$myRequest({
					url:"/api/lunbo/images/"
				})
				console.log(res)
				this.swiperList=res.data.message					
			},
			async getGoods(){
				const res=await this.$myRequest({
					url:"/api/lunbo/goods/1"
				})
				// console.log(res)
				this.goods=res.data.message
			},
			navitemClick(url){
				uni.navigateTo({
					url
				})
			},
			goDetail(id){
				// console.log("id",id) s
				uni.navigateTo({
					url:"/pages/goods-detail/goods-detail?id="+id
				})
			}
			
		}
	}
</script>

<style lang="scss">
	.home{
		swiper{
			width:750rpx;
			height:380rpx;
			image:{
				width: 60%;
				height: 100%;
			}
		}
		.nav{
			display: flex;
			margin-top: 10rpx;
			.nav_item{
				width: 25%;
				text-align: center;
				view{
					width: 120rpx;
					height: 120rpx;
					background-color: $shop-color;
					border-radius: 60rpx;
					margin: 10rpx auto;
					line-height: 120rpx;
					color: #FFFFFF;
					font-size: 50rpx;
				}
				text{
					font-size: 30rpx;
				}
			}
		}
		.hot_goods{
			background-color: #eee;
			overflow: hidden;
			margin-top: 20rpx;
			.tit{
				height: 100rpx;
				line-height: 100rpx;
				color: $shop-color;
				text-align: center;
				letter-spacing: 40rpx;
				background-color: #fff;
				margin: 10rpx 0;
				font-size: 60rpx;
			}

		}
	}
</style>
