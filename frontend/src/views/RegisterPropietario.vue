<template>
  <div class="registerPropietario">
    <!------ Include the above in your HEAD tag ---------->

    <div class="container register-form">

    <form v-on:submit.prevent="registeruser">
      <div class="form">
        <div class="note">
          <p>This is a simpleRegister .</p>
        </div>
        <div class="form-content">
             <div class="form-group">
                       <input type="text" class="form-control" name="name" placeholder="Your Name *" value="" v-model="name"/>
                </div>

              

                <div class="form-group">
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
  name: "registerPropietario",
  components: {},
  data: function () {
    return {
      name: "",
    
      url: "https://prediosbackend.herokuapp.com/",
    };
  },
  methods: {
    registeruser() {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": 'Token '+localStorage.getItem('token'),
      };

      const data = {
        name: this.name,
       
      };

      let self = this

      axios
        .post(
          this.url + "api/propietario_create/",data,
          {
            headers: headers,
          }
          
        )
        .then(function (response) {
          



          console.log(response.status);
          if (response.status == 200 || response.status == 201) {
             alert("El propietario fue creado con éxito!");
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
