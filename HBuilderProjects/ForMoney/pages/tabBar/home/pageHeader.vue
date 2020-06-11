<template>
	<view class="Header">
		<!-- 定位城市 -->
		<view class="addr">
			<view class="icon font">&#xe651;</view>{{city}}
		</view>
		<view class="input-box">
			<input type="text" placeholder="input" placeholder-style="color:#c0c0c0"/>
			<view class="icon font">&#xe61c;</view>
		</view>
		<view class="icon-btn">
			<view class="icon font">&#xe619;</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				city:"北京"
			}
		}
	}
</script>

<style>
</style>
