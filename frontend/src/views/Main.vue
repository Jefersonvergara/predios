
<template>


    <div class="main">

    <nav class="navbar navbar-expand-lg navbar-light bg-light navbar navbar-dark bg-dark">
    
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
            <a class="nav-link" href="/register/">Registar Usuario <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
        </li>
        </ul>
        <span class="navbar-text">
        
        </span>
    </div>

    </nav>
    <div class="list-group">
          
            <a href="/register/" class="list-group-item list-group-item-action">Registar Usuario</a>
            <a href="/propietario/" class="list-group-item list-group-item-action">Añadir propietario</a>
            <a href="/propiedades/" class="list-group-item list-group-item-action">Añadir propiedadesc</a>
            <a href="/listarpropiedades/" class="list-group-item list-group-item-action ">listar Propiedades</a>
    </div>
    </div>

</template>

<script>

//var axios = require('axios');
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'main',
    components: {
    
    },
    data: function(){
    return{

        
        }
    },
    methods:{
        
    }
}


</script>
<style scoped>

</style>