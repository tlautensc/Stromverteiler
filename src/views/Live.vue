<template>
  <div class="home">
    <h1>Live</h1>
    <div class="md-layout md-gutter md-alignment-center">
      <div class="md-layout-item md-xlarge-size-33 md-large-size-33 md-size-medium-33 md-small-size-50 md-xsmall-size-100">
            <iframe src="http://localhost:3000/d-solo/bOCUe4WGz/test-dashboard?orgId=1&from=1592555714590&to=1592577314591&panelId=2&refresh=1s" width="350" height="500" frameborder="0"></iframe>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Live'

}
</script>

<style lang="scss" scoped>
@import "~vue-material/dist/theme/engine"; // Import the theme engine 

  .md-layout-item {
    margin-top: 8px;
    margin-bottom: 8px;

    &:after {
      width: 100%;
      background: md-get-palette-color(red, 200);
    }
  }
</style>