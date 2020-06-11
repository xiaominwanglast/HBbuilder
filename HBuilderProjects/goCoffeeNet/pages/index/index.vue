<template>
	<view>
		<view v-if="showHeader" class="status" :style="{ position: headerPosition,top:statusTop,opacity: afterHeaderOpacity}"></view>
		<view v-if="showHeader" class="header" :style="{ position: headerPosition,top:headerTop,opacity: afterHeaderOpacity }">
			<view class="addr">
				{{ city }}
				<image  src="../../static/iconfont/city.png" ></image>
			</view>
			<view class="input-box">
				<input
					placeholder="点击搜索附近网吧超市"
					placeholder-style="color:#c0c0c0;"
					@tap="toSearch()"
				/>
				<view class="icon search"></view>
			</view>
			<view class="icon-btn" @click="turnToWeather">
				<view class="header_weather">天气</view>
				<image src="../../static/iconfont/weather.png"></image>
			</view>
		</view>
		<view v-if="showHeader" class="place"></view>
		<view class="swiper">
			<view class="swiper-box">
				<swiper circular="true" autoplay="true" @change="swiperChange">
					<swiper-item v-for="swiper in swiperList" :key="swiper.id">
						<image mode="scaleToFill" :src="swiper.img"></image>
					</swiper-item>
				</swiper>
				<view class="indicator">
					<view
						class="dots"
						v-for="(swiper, index) in swiperList"
						:class="[currentSwiper >= index ? 'on' : '']"
						:key="index"
					></view>
				</view>
			</view>
		</view>
		<view class="nav">
			<view class="nav_item" v-for="(item,index) in navs" :key="index" @click="navitemClick(item.url,item.title)">
				<image :src="item.icon"></image>
				<text>{{item.title}}</text>
			</view>
		</view>
		<view class="border"></view>
		<view class="tuijian">
			<view class="tuijian_title">
				<text>附近网吧</text>
				<text @click="findMoreCoffee">更多网吧</text>
				<image src="/static/iconfont/goright.png"></image>
			</view>
			<view class="tuijian_content">
				<view class="tuijian_item" v-for="(item,index) in coffeeList" :key="index" @click="turntomap(item.lat,item.lng)">
					<image style="height: 60px;" src="../../static/iconfont/coffeenet.png"></image>
					<view class="tuijian_content_text">
						<text>{{item.name.length>5?item.name.slice(0,5)+'·':item.name}}</text>
						<text>#{{item.distance}}</text>
					</view>
				</view>
			</view>
		</view>
		<view class="tuijian">
			<view class="tuijian_title">
				<text>附近超市</text>
				<text @click="findMoreShop">更多超市</text>
				<image src="/static/iconfont/goright.png"></image>
			</view>
			<view class="tuijian_content">
				<view class="tuijian_item" v-for="(item,index) in shopList" :key="index" @click="turntomap(item.lat,item.lng)">
					<image style="height: 60px;" src="../../static/iconfont/shop.png"></image>
					<view class="tuijian_content_text">
						<text>{{item.name.length>5?item.name.slice(0,5)+'·':item.name}}</text>
						<text>#距离{{item.distance}}</text>
					</view>
				</view>
			</view>
		</view>
		<view class="border"></view>
	</view>
</template>

<script>
	export default {
		data(){
			return{
				showHeader:true,
				afterHeaderOpacity: 1,//不透明度
				headerPosition: 'fixed',
				headerTop:null,
				statusTop:null,
				nVueTitle:null,
				city: '',
				currentSwiper: 0,
				// 轮播图片
				swiperList: [
					{ id: 1, img: '/static/images/lol1.jpeg' },
					{ id: 2, img: '/static/images/lol2.jpg' },
					{ id: 3, img: '/static/images/dnf1.jpeg' }
				],
				keyword:"",
				latitude:0,
				longitude:0,
				scale:16,
				shopList:[],
				coffeeList:[],
				navs:[
					{
						title:"花椒直播",
						icon:"../../static/video/huajiao.png",
						url:"http://h.huajiao.com"
					},
					{
						title:"虎牙直播",
						icon:"../../static/video/huya.png",
						url:"https://m.huya.com"
					},					{
						title:"斗鱼直播",
						icon:"../../static/video/douyu.png",
						url:"https://m.douyu.com"
					},					{
						title:"YY直播",
						icon:"../../static/video/yy.png",
						url:"https://wap.yy.com"
					}
				]
			}
		},
		onLoad() {
			this.getCity() 
		},
		methods:{
			getCity(){
				uni.getLocation({
					type: 'wgs84',
					success: (data)=> {
						this.getCulot(data.latitude,data.longitude)
					},
					fail:(err) =>{
						console.log(err)
					}
				})
			},
			async getCulot(lat,lng){
				const res=await this.$myRequest({
					url:"api/map/getcity/?lat="+lat.toString()+"&lng="+lng.toString()
				})
				this.city=res.data.message.city
				this.latitude=res.data.message.latitude
				this.longitude=res.data.message.longitude
				this.getCoffee(this.latitude,this.longitude)
				this.getShop(this.latitude,this.longitude)
				uni.setStorage({
				    key: 'location',
				    data: 'lat='+this.latitude.toString()+'&lng='+this.longitude.toString()
				})
			},
			async getShop(lat,lng){
				const res=await this.$myRequest({
					url:"api/map/getshop/?lat="+lat.toString()+"&lng="+lng.toString()
				})
				this.shopList=res.data.message.slice(0,2)
			},
			async getCoffee(lat,lng){
				const res=await this.$myRequest({
					url:"api/map/getcoffee/?lat="+lat.toString()+"&lng="+lng.toString()
				})
				this.coffeeList=res.data.message.slice(0,4)
			},
			getSystem(){
				uni.getSystemInfo({
					success: (res) => {
						console.log(res.brand)
						console.log(res.model)
						console.log(res.version)
					}
				})
			},
			turntomap(lat,lng){
				uni.navigateTo({
					url:"../map/map?"+"lat="+lat.toString()+"&lng="+lng.toString()+"&local_lat="+this.latitude.toString()+"&local_lng="+this.longitude.toString()
				})
			},
			turnToWeather(){
				uni.switchTab({
					url:"/pages/weather/weather"
				})
			},
			findMoreCoffee(){
				uni.getStorage({
					key:"location",
					success:(res) => {
						console.log(res.data)
						uni.navigateTo({
							url:"/pages/moreData/moreData?"+res.data+"&type=coffee",							
						})
					}
				})
			},
			findMoreShop(){
				uni.getStorage({
					key:"location",
					success:(res) => {
						console.log(res.data)
						uni.navigateTo({
							url:"/pages/moreData/moreData?"+res.data+"&type=shop",							
						})
					}
				})
			},
			//搜索跳转
			toSearch() {
				uni.switchTab({
					url:"/pages/coffee/coffee"
				})
			},
			navitemClick(url,title){
				uni.navigateTo({
					url:"/pages/video/video?url="+url+"&title="+title
				})
			},
			//轮播图指示器
			swiperChange(event) {
				this.currentSwiper = event.detail.current;
			},
		}
	}
</script>

<style lang="scss" scoped>
	.status {
		width: 100%;
		height: 0;
		position: fixed;
		z-index: 10;
		background-color: #fff;
		top: 0;
		/*  #ifdef  APP-PLUS  */
		height: var(--status-bar-height); //覆盖样式
		/*  #endif  */
	}
	.header {
		width: 92%;
		padding: 0 4%;
		height: 100upx;
		display: flex;
		align-items: center;
		position: fixed;
		top: 0;
		z-index: 10;
		background-color: #fff;
	
		/*  #ifdef  APP-PLUS  */
		top: var(--status-bar-height);
		/*  #endif  */
	
		.addr {
			width: 160upx;
			height: 60upx;
			flex-shrink: 0;
			display: flex;
			align-items: center;
			font-size: 35upx;
			image{
				margin-right: 5upx;
				height: 20px;
				width: 20px;
			}
		}
		.input-box {
			width: 100%;
			height: 60upx;
			background-color: #f5f5f5;
			border-radius: 20upx;
			position: relative;
			display: flex;
			align-items: center;
			.icon {
				display: flex;
				align-items: center;
				position: absolute;
				top: 0;
				right: 0;
				width: 60upx;
				height: 60upx;
				font-size: 34upx;
				color: #c0c0c0;
			}
			input {
				padding-left: 28upx;
				height: 28upx;
				font-size: 30upx;
			}
		}
		.icon-btn {
			width: 180upx;
			height:55upx;
			flex-shrink: 0;
			display: flex;
			.header_weather{
				width: auto;
				padding-left: 20px;
			}
			image {
				width: 50upx;
				height: 50upx;
				display: flex;
				justify-content: flex-end;
				align-items: center;
			}
		}
	}
	.place {
		background-color: #ffffff;
		height: 100upx;
		/*  #ifdef  APP-PLUS  */
		margin-top: var(--status-bar-height);
		/*  #endif  */
	}
	.swiper {
		width: 100%;
		margin-top: 10upx;
		display: flex;
		justify-content: center;
		.swiper-box {
			width: 92%;
			height: 30.7vw;
	
			overflow: hidden;
			border-radius: 15upx;
			box-shadow: 0upx 8upx 25upx rgba(0, 0, 0, 0.2);
			//兼容ios，微信小程序
			position: relative;
			z-index: 1;
			swiper {
				width: 100%;
				height: 30.7vw;
				swiper-item {
					image {
						width: 100%;
						height: 30.7vw;
					}
				}
			}
			.indicator {
				position: absolute;
				bottom: 20upx;
				left: 20upx;
				background-color: rgba(255, 255, 255, 0.4);
				width: 150upx;
				height: 5upx;
				border-radius: 3upx;
				overflow: hidden;
				display: flex;
				.dots {
					width: 0upx;
					background-color: rgba(255, 255, 255, 1);
					transition: all 0.3s ease-out;
					&.on {
						width: (100%/3);
					}
				}
			}
		}
	}
	.banner {
		width: 92%;
		margin: 0upx 4%;
		image {
			width: 100%;
			height: 30vw;
			border-radius: 10vw;
			box-shadow: 0upx 5upx 25upx rgba(0, 0, 0, 0.3);
		}
	}
	.nav{
		display: flex;
		margin-top: 20rpx;
		.nav_item{
			width: 25%;
			height: 100px;
			text-align: center;
			background-color: #FFFAFA;
			image{
				width: 130rpx;
				height: 130rpx;
				margin: 5rpx 20rpx;
				text-align: center;
			}
			text{
				font-size: 30rpx;
			}
		} 
	}
	.border{
		border: 2px solid #C0C0C0;
	}
	.tuijian{
		padding-top: 3px;
		font-size: 20;
		.tuijian_title{
			display: flex;
			width: 100%;
			height: 25px;
			image{
				height: 18px;
				width: 18px;
				margin-top: 14rpx;
			}
			text{
				margin-left: 10px;
			}
			text:nth-child(2) {
				font-size: 15px;
				margin-top: 10rpx;
				margin-left: 200px;
			}
		}
		.tuijian_content{
			uni-image{
				height: 62px;
			}
			font-size: 25px;
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
			background-color: #FFFAFA;
			.tuijian_item{
				width: 370rpx;
				margin: 10rpx 0;	
				display: flex;
				image{
					heigh:60px;
					width:70px;
				}
				.tuijian_content_text{
					font-size: 35rpx;
					display: flex;
					width: 130px;
					flex-direction:column;
					text{
						margin-top: 10px;
					}
					text:nth-child(2){
						color: #FF7256;
						font-size: 28rpx;
						margin-left: 20rpx;
					}
				}
			}
		}
	}
</style>
