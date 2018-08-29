import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import App from '@/App.vue'
import IndexBody from '@/views/index/IndexBody.vue'
import Msg from '@/views/Msg.vue'
import Login from '@/views/Login.vue'
import Home from '@/views/Home.vue'

import Test from '@/components/Test.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: App,
      children: [
        {
          path: "index",
          component: IndexBody
        },
        {
          path: "login",
          component: Login
        },
        {
          path: "home",
          component: Home
        }
      ]
    },
    {
      path: "/msg",
      component: Msg
    },
    {
      path: '/test',
      component: Test
    }
  ]
})
