<template>
  <q-layout view="hHh lpR fFf">

    <q-header reveal bordered class="bg-indigo-9 text-white center">
      <q-toolbar >
        <q-toolbar-title @click="backHome" class="text-center">
          <span class="cursor-pointer">
            <span class="special-letter">E</span>volutionary 
            <span class="special-letter">L</span>earning-Derived 
            <span class="special-letter">M</span>ultimodal Models 
            for Predicting
            <span class="special-letter">E</span>arly 
            <span class="special-letter">R</span>ecurrence 
            after 
            <span class="special-letter">S</span>urgery 
            of 
            <span class="special-letter">L</span>iver Cancer
            
              </span>
        </q-toolbar-title>
        
      </q-toolbar>
    </q-header>


    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer reveal bordered class="footer-bg text-black no-border">
      <q-toolbar>
        <!-- 版本信息 -->
        <q-toolbar-title >
          <div class="text-caption text-center">&copy; 2023 Yang Ming Chiao Tung University Intelligent Computation Laboratory  All rights reserved.</div>
        </q-toolbar-title>

        <div class="footer-images ">
        <q-img
          src="../pic/北榮logo.png"
          style="height: 75px; width: 75px; ;"
        />
        <q-img
          src="../pic/陽明交大校徽.jpeg"
          style="height: 75px; width: 75px;"
        />
      </div>
      </q-toolbar>
      <!-- 图片容器 -->
      
    </q-footer>

  </q-layout>

  
</template>

<script>
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'


export default defineComponent({
  name: 'MainLayout',

  setup () {
    const $router = useRouter()

    const backHome = () =>{
      $router.push('/')
    }

    return {backHome}
  }
})
</script>
<style>
.q-page-container {
  /* background-image: url('../pic/0738.gif'),url('../pic/9142.jpg'); */
  background-size: 40%,35%; /* 或者其他如 'contain', '100% 100%' 等 */
  background-position: bottom right,bottom left;
  background-repeat: no-repeat,no-repeat;
}
.footer-images {
  text-align: center;
}
.footer-bg {
  background-color: rgba(0, 0, 0, 0.2); /* 白色背景，50% 透明度 */
}
.no-border {
  border: none !important; /* 移除边框 */
}
.cursor-pointer {
  font-family: 'Times New Roman', serif;
}

.special-letter {
  font-style: italic;
  color: red;
}
</style>