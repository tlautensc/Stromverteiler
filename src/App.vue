<template>
  <div id="app">
    <div class="page-container">
      <md-app md-waterfall md-mode="overlap">
        <md-app-toolbar class="md-primary md-large">
          <div class="md-toolbar-row">
            <md-button class="md-icon-button" @click="$router.back()" v-if="!(this.$route.name == 'Home') && !(this.$route.name == 'Login')">
              <md-icon>arrow_back</md-icon>
            </md-button>
            
            <span class="md-title" style="color: white">Buchrezept</span>
            <md-button class="md-icon-button" style="position: fixed; right: 0" @click="reloadPage" >
              <md-icon>refresh</md-icon>
            </md-button>
          </div>
        </md-app-toolbar>

        <md-app-content style="margin-bottom: 60px;">
          <router-view/>
        </md-app-content>
      </md-app>
    </div>
    <div class="phone-viewport">
      <md-bottom-bar md-sync-route md-mode="shift">
        <md-bottom-bar-item style="max-width: none" to="/" exact md-icon="home"></md-bottom-bar-item>
        <md-bottom-bar-item style="max-width: none" to="/add" md-icon="add"></md-bottom-bar-item>
        <md-bottom-bar-item style="max-width: none" to="/settings" md-icon="settings"></md-bottom-bar-item>
      </md-bottom-bar>
    </div>
  </div>
</template>

