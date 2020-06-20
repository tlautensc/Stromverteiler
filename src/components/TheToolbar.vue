<template>
<div>
    <div class="md-toolbar-row">
        <div class="md-toolbar-section-start">
            <md-button class="md-icon-button" @click="makeVisible">
                <md-icon>menu</md-icon>
            </md-button>
            <h3 class="md-title">Tontechnik Butz</h3>
        </div>
    </div>
    
</div>
  
</template>

<script>
export default {
    name: 'TheToolbar',
    methods: {
        makeVisible() {
            this.$emit('makeVisible')
        },
    },

}
</script>

<style>

</style>