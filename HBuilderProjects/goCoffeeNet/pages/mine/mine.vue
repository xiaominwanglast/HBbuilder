<template>
	<view>
		<view v-if="showHeader" class="status" :style="{position:headerPosition,top:statusTop}"></view>
		<view v-if="showHeader" class="header" :style="{position:headerPosition,top:headerTop}">
			<view class="addr"></view>
			<view class="input-box">
			</view>
		</view>
		<!-- 占位 -->
		<view v-if="showHeader" class="place"></view>
		<!-- 用户信息 -->
		<view class="user">
			<!-- 头像 -->
			<view class="left">
				<image :src="user.face"></image>
			</view>
			<!-- 昵称,个性签名 -->
			<view class="right">
				<view class="username">{{user.username}}</view>
				<!-- <view class="signature" @tap="toSetting">{{user.signature}}</view> -->
			</view>
			<!-- 二维码按钮 -->
			<view class="erweima">
				<view class="icon qr"></view>
			</view>
		</view>
		<!-- VIP banner -->
		<view class="VIP">
			<view class="img">
				<image src="/static/images/VIP.png"></image>
			</view>
			<view class="title">后续开通VIP会员</view>
			<view class="tis">会员特权</view>
		</view>
		<view class="list">
			<view class="row">
				<view class="title">版本升级</view>
				<view class="right"><view class="tis"><text>v1.1.4</text></view></view>
			</view>
			<view class="row">
				<view class="title">清除缓存</view>
				<view class="right"><view class="tis"><text @click="clearData">点击清理</text></view></view>
			</view>
			<view class="row">
				<view class="title">问题反馈</view>
				<view class="right"><view class="tis"><text></text></view></view>
			</view>
			<view class="row">
				<view class="title">关于开发者</view>
				<view class="right"><view class="tis"><text>生活奔波</text></view></view>
			</view>
			<view class="row">
				<view class="title">关于语言</view>
				<view class="right"><view class="tis"><text>uniApp</text></view></view>
			</view>
			<view class="row">
				<view class="title">关于位置</view>
				<view class="right"><view class="tis"><text>上海浦东新区</text></view></view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				isfirst:true,
				headerPosition:"fixed",
				headerTop:null,
				statusTop:null,
				showHeader:true,
				//个人信息,
				user:{
					username:'游客1002',
					face:'/static/images/face.jpg',
					signature:'后续转登录/注册页',
					integral:0,
					balance:0,
					envelope:0
				},
			}
		},
		methods:{
			clearData(){
				uni.showToast({
					icon:"success",
					title:"清理完成"
				})
			}
		}
	}
</script>

<style lang="scss">
	page{position: relative;background-color: #fff;}
	.status {
		width: 100%;
		height: 0;
		position: fixed;
		z-index: 10;
		background-color: #f06c7a;
		top: 0;
		/*  #ifdef  APP-PLUS  */
		height: var(--status-bar-height);//覆盖样式
		/*  #endif  */
		
	}
	.header{
		width: 92%;
		padding: 0 4%;
		height: 100upx;
		display: flex;
		justify-content: flex-end;
		align-items: center;
		position: fixed;
		top: 0;
		z-index: 10;
		background-color: #f06c7a;
		/*  #ifdef  APP-PLUS  */
		top: var(--status-bar-height);
		/*  #endif  */
		.icon-btn{
			width: 120upx;
			height: 60upx;
			flex-shrink: 0;
			display: flex;
			.icon{
				color: #fff;
				width: 60upx;
				height: 60upx;
				display: flex;
				justify-content: flex-end;
				align-items: center;
				font-size: 42upx;
			}
		}
	}
	.place{
		background-color: #f06c7a;
		height: 100upx;
		/*  #ifdef  APP-PLUS  */
		margin-top: var(--status-bar-height);
		/*  #endif  */
	}
	.place-bottom{
		height: 300upx;
	}
	.user{
		width: 92%;
		padding: 0 4%;
		display: flex;
		align-items: center;
		// position: relative;
		background-color: #f06c7a;
		padding-bottom: 120upx;
		.left{
			width: 20vw;
			height: 20vw;
			flex-shrink: 0;
			margin-right: 20upx;
			border: solid 1upx #fff;
			border-radius: 100%;
			image{
				width: 20vw;
				height: 20vw;
				border-radius: 100%;
			}
			
		}
		.right{
			width: 100%;
			.username{
				font-size: 36upx;
				color: #fff;
			}
			.signature{
				color: #eee;
				font-size: 28upx;
			}
		}
		.erweima{
			flex-shrink: 0;
			width: 10vw;
			height: 10vw;
			margin-left: 5vw;
			border-radius: 100%;
		
			display: flex;
			justify-content: center;
			align-items: center;
			background: linear-gradient(to left, #fbbb37 0%,#fcf0d0 105%);
			.icon{
				color: #7b6335;
				font-size: 42upx;
			}
		}
	}
	.VIP{
		width: 84%;
		margin: -65upx auto 20upx auto;
		padding: 30upx 4%;
		background: linear-gradient(to left, #dea96d 0%,#f6d59b 100%);
		box-shadow: 0upx 0upx 25upx rgba(0,0,0,0.2);
		border-radius: 15upx;
		display: flex;
		align-items: center;
		.img{
			flex-shrink: 0;
			width: 60upx;
			height: 60upx;
			image{
				width: 60upx;
				height: 60upx;
			}
		}
		.title{
			width: 100%;
			color: #796335;
			font-size: 30upx;
		}
		.tis{
			width: 100%;
			display: flex;
			justify-content: flex-end;
			color: #fcf0d0;
			font-size: 26upx;
		}
	}
	.list{
		width: 96%;
		padding-top: 30px;
		padding-left: 4%;
		background-color: #fff;
		margin-bottom: 20upx;
		.row{
			widows: 100%;
			min-height: 90upx;
			display: flex;
			align-items: center;
			justify-content: space-between;
			border-bottom: solid 1upx #eee;
			&:last-child{
				border-bottom: none;
			}
			.title{
				font-size: 32upx;
				color: #333;
			}
			.right{
				display: flex;
				align-items: center;
				color: #999;
				.tis{
					font-size: 26upx;
					margin-right: 5upx;
					max-height: 120upx;
					image{
						width: 100upx;
						height: 100upx;
						border-radius: 100%;
						margin: 10upx 0;
					}
					text{
						margin-right: 10px;
					}
				}
				.icon{
					width: 40upx;
					color: #cecece;
				}
			}
			
		}
		}
</style>
