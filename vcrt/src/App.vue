<template>
    <div>
      <div class="index-header">
        <div class="index-header-face">
          <img :src="user.user_face" v-if="!is_login"> 
          <img :src="user.user_face" v-else class="logined-img" @click="logout()"> 
        </div>
        <div class="index-header-name">
          <p v-if="page_flag === 'index'">
            Welcome to VcrT, <router-link to="/login">click here</router-link><span> to login you Account.</span>
          </p>
          <p v-if="page_flag === 'login'">
            <p v-if="!is_login">
              <router-link to="/login">Login you account</router-link>
            </p>
            <p v-else>
              <router-link to="/login">{{ user.user_name }}</router-link>
            </p>
          </p>
        </div>
      </div>
      <div class="index-body"> 
        <router-view></router-view>
      </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      page_flag: "login",
      is_login: false,
      user: {
        'user_face': '../static/assets/Contact.png',
        'user_name': 'VcrT'
      }
    }
  },
  mounted () {
    this.$pubsub.subscribe('login', (is_login, user) => {
      this.is_login = true
      this.get_user()
    })
    this.login_status()
  },
  methods: {
    set_user (user) {
      this.$sql.save_data(user, 'lucy')
      this.user = user
    },
    get_user () {
      const user = this.$sql.read_data('lucy')
      user.user_face = this.$web_conf.MEDIA_URL + user.user_face
      this.user = user
    },
    login_status () {
      const user = this.$sql.read_data('lucy')
      if (user) {
        user.user_face = this.$web_conf.MEDIA_URL + user.user_face
        this.user = user
        this.is_login = true
      }
      else {
        this.is_login = false
        this.user = {
          'user_face': '../static/assets/Contact.png',
          'user_name': 'VcrT'
        }
      }
    },
    logout () {
      if (window.confirm('You will log out you account, are you suer ?')) {
        this.$sql.remove_data('lucy')
        window.location.reload()
      }
    }
  }
}
</script>

<style>
.index-header {
  width: 100%;
  position: fixed;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
}
.index-header-face {
  width: 45px;
  height: 45px;
  background-color: #00a8f3;
  float: left;
}
.index-header-face img {
  width: auto;
  height: 45px;
  float: left;
}
.logined-img {
  border: none;
}
.logined-img:hover {
  border: none;
}
.index-header-name {
  float: left;
  height: 45px;
}
.index-header-name p {
  float: left;
  margin-left: 6px;
}
.index-header-name p span {
  color: rgba(48, 48, 48, 1);
}

.index-body {
  margin-top: 43px;
  z-index: 100;
}

.index-footer {
  width: 100%;
  float: left;
}
</style>
