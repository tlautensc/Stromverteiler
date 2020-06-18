<template>
<div>
    <div class="md-toolbar-row">
        <div class="md-toolbar-section-start" @click="makeVisible">
            <md-button class="md-icon-button">
                <md-icon>menu</md-icon>
            </md-button>
        </div>
    </div>
    <div class="md-toolbar-row md-toolbar-offset">
        <h3 class="md-title">Tontechnik Butz</h3>
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