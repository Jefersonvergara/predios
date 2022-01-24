
<template>
  <gmap-map
    :center="center"
    :zoom="16"
    style="width: 100%; height: 500px"
  >
    <gmap-marker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :title="m.title"
      :clickable="true"
      :draggable="true"
      @click="center=m.position"
      @drag="updateCoordinates"
    ></gmap-marker>
  </gmap-map>
</template>
<script>
  export default {
    data () {
      return {
        coordinates: null,
        center: {lat: this.latitude, lng: this.longitude},
        markers: [{
          position: {lat: this.latitude, lng: this.longitude},
          title: this.title
        }]
      }
    },

    methods: {
        updateCoordinates(location) {
            this.coordinates = {
                lat: location.latLng.lat(),
                lng: location.latLng.lng(),
            };
          
        },
    },

    props: {
        latitude: Number,
        longitude: Number,
        title: String
    }
  }
</script>
