<template>
  <div class="registerPropiedades">
    <!------ Include the above in your HEAD tag ---------->

    <div class="container register-form">

    <form v-on:submit.prevent="registeruser">
      <div class="form">
        <div class="note">
          <p>This is a simpleRegister .</p>
        </div>
        <div class="form-content">
                <div class="form-group">
                       <input type="text" class="form-control" name="direccion" placeholder="direccion *" value="" v-model="direccion"/>
                </div>

                <div class="form-group">
                <label for="">Propietario</label>
                <select v-model="propietario" name="propietario" class="form-control">
                <option></option>
                <option v-for="item in propietarios" :value="item.id" :key="item.id">
                  {{ item.name }}
                </option>
              </select>
                </div>


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
      :draggable="true"
      @click="center=m.position"
      @drag="updateCoordinates"
    ></gmap-marker>
  </gmap-map>

  <div class="form-group">
                       <input type="text" class="form-control" name="lat" placeholder="lat *"   v-model="lat"/>
                </div>

  <div class="form-group">
                       <input type="text" class="form-control" name="lng" placeholder="long *"   v-model="lng"/>
                </div>
                
                <input type="submit" class="btnSubmit" value="Enviar">
                </div>

         </div>           
            </div>
            
        </form>

    </div>


  </div>

  
</template>

<script>
var axios = require("axios");



export default {
  name: "registerPropiedades",
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
          title: "prueba"
        }],

      name: "",
      direccion:"",

      propietarios: [],
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
        
    registeruser() {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": 'Token '+localStorage.getItem('token'),
      };

      const data = {
    address:this.direccion ,
    latitud:this.lat ,
    longitud:this.lng ,
    propietario:this.propietario 
      };

      let self = this

      axios
        .post(
          this.url + "api/propiedades_create/",data,
          {
            headers: headers,
          }
          
        )
        .then(function (response) {
          



console.log(response.status);
    if (response.status == 200 || response.status == 201) {
      alert("L propiedad fue creado con éxito!");
            self.$router.push('/main/');
          } else {
            alert("Datos no validos");
          }
        })
        .catch(function (error) {
          try {
            alert(error.response.data.non_field_errors[0]);
          } catch {
            alert(error.response.data);
          }
        });
    },
  },



  mounted() {
     

      const headers = {
        "Content-Type": "application/json",
        "Authorization": 'Token '+localStorage.getItem('token'),
      };

      axios
        .get(
          this.url + "api/propietario_list/",
          {
            headers: headers,
          }).then(response => (this.propietarios = response.data))
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
