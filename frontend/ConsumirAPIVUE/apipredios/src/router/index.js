import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Main from '../views/Main.vue'
import RegisterUsuario from '../views/RegisterUser.vue'
import RegisterPropietario from '../views/RegisterPropietario.vue'
import ListarPropiedades from '../views/ListarPropiedades.vue'
import RegisterPropiedades from '../views/RegisterPropiedades'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  },
  {
    path: '/register',
    name: 'RegisterUsuario',
    component: RegisterUsuario 
  },
  {
    path: '/propietario',
    name: 'RegisterPropietario',
    component: RegisterPropietario 
  },
  {
  path: '/propiedades',
  name: 'RegisterPropiedades',
  component: RegisterPropiedades 
},
{
path: '/listarpropiedades',
name: 'ListarPropiedades',
component: ListarPropiedades 
},




  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
