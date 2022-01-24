<template>
  <div class="listarPropiedades">
    <!------ Include the above in your HEAD tag ---------->

    <div class="container register-form">

   
        <div class="note">
          <p>Lista de propiedades.</p>
        </div>
        <div class="form-content">
               <div class="row">
               
               <div class="col-6">
              <ul class="list-group">
              <li v-for="item in propiedades" v-on:click="updatelist(item.latitud,item.longitud)" :key="item.id" class="list-group-item"><b>{{item.propietario_name}}</b> {{item.address}}</li>
               </ul>  

               </div>

               <div class="col-6">
              
                <div class="form-group">

                 <gmap-map
    :center="center"
    :zoom="16"
    style="width: 100%; height: 300px"
  >
    <gmap-marker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :title="m.title"
      :clickable="true"
      :draggable="false"
      @click="center=m.position"
      @drag="updateCoordinates"
    ></gmap-marker>
  </gmap-map>

  

  
                
              
                </div>

               </div>

               </div>

            



         </div>           
           

    </div>


  </div>

  
</template>

<script>
var axios = require("axios");



export default {
  name: "listarPropiedades",
  components: {
   
  },
  data: function () {
    return {
      accessToken: 'pk.eyJ1IjoiYWNtZWppYTcyNyIsImEiOiJjamx6bWxnbmswMTFrM2txd2g4eG1ldGx0In0.C9BA7McWtWqCH98qyAd3pg', // your access token. Needed if you using Mapbox maps
      mapStyle: 'mapbox://styles/mapbox/streets-v11', // your map style

        lat:"6.259663",
        lng:"-75.571837",
        coordinates: null,
        center: {lat: 6.259663, lng:  -75.571837},
        markers: [{
          position: {lat: 6.259663, lng:  -75.571837},
         
        }],

      name: "",
      direccion:"",

      propiedades: [],
      propietario:'',
      coord:null,
      url: "http://127.0.0.1:8100/",
    };
  },
  methods: {

    updateCoordinates(location) {
              
                this.lat =  location.latLng.lat()
                this.lng = location.latLng.lng()
           
            
        },

    updatelist(lat,lng){
        //lat = lat.replace('.', ',');
        //lng = lng.replace('.', ',');
        console.log(lat,lng)
        this.center = {lat: parseFloat(lat), lng:  parseFloat(lng)}
        console.log(this.center)
        this.markers =  [{
          position: {lat: parseFloat(lat), lng:  parseFloat(lng)},
         
        }]
        //this.markers.position.lat = lat
        //this.markers.position.lng = lng
    }
        
    
  },



  mounted() {
     

      const headers = {
        "Content-Type": "application/json",
        "Authorization": 'Token '+localStorage.getItem('token'),
      };

      axios
        .get(
          this.url + "api/propiedades_list/",
          {
            headers: headers,
          }).then(response => (this.propiedades = response.data))
        .catch(function (error) {
          try {
            alert(error.response.data.non_field_errors[0]);
          } catch {
            alert(error.response.data);
          }
        });
          
  }
};
</script>
<style scoped>

.note {
  text-align: center;
  height: 80px;
  background: -webkit-linear-gradient(left, #0072ff, #8811c5);
  color: #fff;
  font-weight: bold;
  line-height: 80px;
}
.form-content {
  padding: 5%;
  border: 1px solid #ced4da;
  margin-bottom: 2%;
}
.form-control {
  border-radius: 1.5rem;
}
.btnSubmit {
  border: none;
  border-radius: 1.5rem;
  padding: 1%;
  width: 20%;
  cursor: pointer;
  background: #0062cc;
  color: #fff;
}
</style>
