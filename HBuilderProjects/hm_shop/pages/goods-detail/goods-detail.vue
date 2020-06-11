<template>
	<view class="goods_details">
		<swiper indicator-dots>
			<swiper-item v-for="(item,index) in gouwutu" :key="index">
				<image :src="item.src"></image>
			</swiper-item>
		</swiper>
		<view class="box1">
			<view class="price">
				<text>￥3000</text>
				<text>￥3500</text>
			</view>
			<view class="goods_name">
				<text>这他吗居然是个手机，我是真的信了，还在等什么，赶紧去拉屎，有点憋不住了</text>
			</view>
		</view>
		<view class="spaceview"></view>
		<view class="box2">
			<view>
				<text>货号:VF1003243</text>
			</view>
			<view>
				<text>库存:103</text>
			</view>
		</view>
		<view class="spaceview"></view>
		<view class="box3">
			<view class="tit">详情简介</view>
			<view class="content">复苏一词，赫然出现在东风悦达起亚过去一年的成绩单上，市场给东风悦达起亚打出了一个尚且不错的成绩，从根本上来说，这离不开体系内做出的多方努力。
去年9月份，李峰出任现代汽车集团（中国）副总裁、东风悦达起亚总经理，作为韩系车国内合资公司的首任中国籍CEO，可以看的出来现代集团决定做好两大合资品牌的决心以及信心。
启用中国籍CEO，深一层次的价值在于中国人更懂中国人需要什么，本土化企业还需本土化人才来操盘，在过去的半年中，李峰作出的成绩太多，我们不能用冰冷的销量数据来衡量。
李峰的职位会比想象中的更大，实权在握直接能调动东风悦达起亚体系，企业最为关键的产、销、营三个业务都交给了李峰，作为拥有多家自主、合资履历的李峰，此次出任东风悦达起亚总经理，从过往工作经验上来说，李峰拥有很强的信心可以做好起亚国内市场。</view>
		</view>
		<view class="goodsnav">
			<uni-goods-nav :fill="true"  :options="options" :button-group="buttonGroup"  @click="onClick" @buttonClick="buttonClick" ></uni-goods-nav>
		</view>	
	</view>
</template>

<script>
	import uniGoodsNav from '@/components/uni-goods-nav/uni-goods-nav.vue'

	export default {
		data() {
			return {
				id:0,
				gouwutu:[],
				options: [{
				  icon: 'https://img-cdn-qiniu.dcloud.net.cn/uniapp/uni-ui/goodsnav/kefu.png',
				  text: '客服'
				}, {
				  icon: 'https://img-cdn-qiniu.dcloud.net.cn/uniapp/uni-ui/goodsnav/dianpu.png',
				  text: '店铺'
				}, {
				  icon: 'https://img-cdn-qiniu.dcloud.net.cn/uniapp/uni-ui/goodsnav/carts.png',
				  text: '购物车',
				  info: 2
				}],
				buttonGroup: [{
				  text: '加入购物车',
				  backgroundColor: '#ff0000',
				  color: '#fff'
				},
				{
				  text: '立即购买',
				  backgroundColor: '#ffa200',
				  color: '#fff'
				}
				]
			}
		},

		components: {uniGoodsNav},

		methods: {
			async getgouwu(){
				const res=await this.$myRequest({
					url:"/api/lunbo/getgouwu/"+this.id
				})
				this.gouwutu=res.data.message
			},
			  onClick (e) {
				uni.showToast({
				  title: `点击${e.content.text}`,
				  icon: 'none'
				})
			  },
			  buttonClick (e) {
				console.log(e)
				this.options[2].info++
			  }
		},
		onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
			// console.log(option.id); //打印出上个页面传递的参数。
			this.id=option.id
			this.getgouwu()
		}
	}
</script>

<style lang="scss">
	.goods_details{
		swiper{
			height: 700rpx;
			image{
				height: 100%;
				width: 100%;
			}
		}
		.box1{
			padding: 10px;
			.price{
				font-size: 35rpx;
				color: $shop-color;
				line-height: 80rpx;
				text:nth-child(2){
					color: #ccc;
					font-size: 28rpx;
					margin-left: 20rpx;
					text-decoration: line-through;
				}
			}
			.goods_name{
				font-size: 30rpx;
				line-height: 50rpx;
			}
		}
		.box2{
			line-height: 60rpx;
			font-size: 30rpx;
		}
		.box3{
			padding-bottom: 60rpx;
			.tit{
				font-size: 35rpx;
				line-height: 50rpx;
				text-align: center;
				border-bottom: 1px solid #C0C0C0;
			}
			.content{
				font-size: 30rpx;
				line-height: 40rpx;
			}
		}
	}
	.spaceview{
		height: 10rpx;
		width: 100%;
		background-color: #ccc;
	}
	.goodsnav{
		position: fixed;
		bottom: 0;
		width: 100%;
	}
</style>
