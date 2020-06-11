<template>
	<view class="goods_list">
		<view class="goods_item" v-for="item in goods" :key="item.id" @click="goDoodsD(item.id)">
			<image :src="item.image_url"></image>
			<view class="price">
				<text>￥{{item.sell_price}}</text>
				<text>￥{{item.market_price}}</text>
			</view>
			<view>
				<text>{{item.title}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		props:["goods"],
		methods:{
			goDoodsD(id){
				this.$emit("goodsItemClick",id)
			}
		}
	}
</script>

<style lang="scss">
	.goods_list{
		padding: 0 15rpx;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		.goods_item{
			background-color: #fff;
			width: 355rpx;
			margin: 10rpx 0;
			padding: 5px;
			box-sizing: border-box;
			image{
				width: 60%;
				height: 160rpx;
				margin-left: 60rpx;
			}
			.price{
				font-size: 35rpx;
				color: $shop-color;
				text:nth-child(2){
					color: #D1D1D1;
					font-size: 25rpx;
					margin-left: 20rpx;
					text-decoration: line-through;
				}
			}
			.name{
				font-size: 28rpx;
				line-height: 50rpx;
				padding-bottom: 20rpx;
				padding-top: 10rpx;
			}
		}
	}
</style>
