import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
    { 
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/live',
      name: 'Live',
      component: () => import('../views/Live.vue'),
    },
    {
      path: '/history',
      name: 'History',
      component: () => import('../views/History.vue'),
    },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
