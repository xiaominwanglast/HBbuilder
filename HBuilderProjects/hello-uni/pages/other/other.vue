<template>
	<view>
	<button @click="updatemsg">点击</button>	
	<view>
		<uni-calendar 
		ref="calendar"
		:insert="false"
		@confirm="confirm"
		 ></uni-calendar>
		 <button @click="open">打开日历</button>
	</view>
	</view>
</template>

<script>
	import uniCalendar from '@/components/uni-calendar/uni-calendar.vue'
	export default{
		data(){
			return{
				msg:0
			}
		},
		onLoad(option) {
			console.log(option)
			uni.setStorageSync("id",option)
		},
		components:[
			uniCalendar
		],
		methods:{
			updatemsg(){
				uni.getStorage({
					key:"id",
					success(res) {
						console.log(res.data.id)
						this.msg=this.msg+res.data.id
					}
				})
			},
			change(e){
				console.log(e)
			},
			open(){
				this.$refs.calendar.open();
			}
		}
	}
</script>

<style>
</style>
