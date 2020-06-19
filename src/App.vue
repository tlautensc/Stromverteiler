<template>
  <div>
    <div v-if="!isMobile()">
      <Computer />
    </div>
    <div v-else>
      <Mobile />
    </div>
  </div>
</template>


<script>
  import Computer from './components/Computer';
  import Mobile from './components/Mobile';
  export default {
    components: {
      Computer,
      Mobile
    },
    name: 'App',
    methods:{
      isMobile(){
        if( screen.width < 660 ) {
          return true;
        }
        else {
          return false;
        }
      },
    }
  }
</script>
