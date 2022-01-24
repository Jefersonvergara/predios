<template>
  <div class="register">
    <!------ Include the above in your HEAD tag ---------->

    <div class="container register-form">

        <form v-on:submit.prevent="registerfn">
    <div class="form">
            <div class="note">
            <p>INGRESE LOS DATOS PARA REGISTRARSE.</p>
        </div>

    <div class="form-content">
        <div class="row">
            <div class="col-md-6">
            <div class="form-group">
                <input
                type="text"
                class="form-control"
                placeholder="usuario *"
                value=""
                name="username"
                v-model="username"
                />
            </div>

            <div class="form-group">
                <input
                type="email"
                class="form-control"
                  placeholder="email *"
                value=""
                name="email"
                v-model="email"
                />
            </div>
        
            </div>
            <div class="col-md-6">
            <div class="form-group">
                <input
               type="text"
                  class="form-control"
                  placeholder="nombre *"
                  value=""
                  name="first_name"
                  v-model="first_name"
                />
              </div>
              <div class="form-group">
                <input
                  type="text"
                  class="form-control"
                  placeholder="apellido *"
                  value=""
                  name="last_name"
                  v-model="last_name"
                />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input
                  type="password"
                  class="form-control"
                  placeholder="contraseña"
                  value=""
                  name="password1"
                  v-model="password1"
                />
              </div>
              <div class="form-group">
                <input
                  type="password"
                  class="form-control"
                  placeholder="Confirmar contraseña"
                  value=""
                  name="password2"
                  v-model="password2"
                />
              </div>
            </div>
          </div>
          <input type="submit" class="btnSubmit" value="Enviar">
        
        </div>
      </div>
      </form>
    </div>
    
  </div>
</template>

<script>
var axios = require("axios");

export default {
  name: "register",
  components: {},
  data: function () {
    return {
      username: "",
      password1: "",
      password2: "",
      first_name: "",
      last_name: "",
      email: "",
      url: "https://prediosbackend.herokuapp.com/",
    };
  },
  methods: {
    registerfn() {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": localStorage.getItem('token'),
      };

      const data = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
      };

      let self = this

      axios
        .post(
          this.url + "api/create/",data,
          {
            headers: headers,
          }
          
        )
        .then(function (response) {
          



          console.log(response.status);
          if (response.status == 200) {
             alert("El usuario fue creado con éxito!");
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
