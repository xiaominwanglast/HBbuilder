<template>
	<view>
		<map class="map" :scale="scale" :latitude="local_lat" :longitude="local_lng" :markers="markers"></map>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				local_lat:0.0,
				local_lng:0.0,
				scale:16,
				markers:[
				]
			}
		},
		methods: {
		},
		onLoad: function (option) { 
			this.local_lat=parseFloat(option.local_lat)
			this.local_lng=parseFloat(option.local_lng)
			this.markers=[
					{
						latitude:parseFloat(option.lat),
						longitude:parseFloat(option.lng),
						iconPath:"../../static/iconfont/location.png",
						width:50,
						heigh:50
					},
					{
						latitude:parseFloat(option.local_lat),
						longitude:parseFloat(option.local_lng),
						iconPath:"../../static/iconfont/location_p.png",
						width:50,
						heigh:50
					},
				]
				console.log(this.markers)
			}
		}

</script>

<style lang="scss">
.map{
	width: 100%;
	height: 500px;
}
</style>
