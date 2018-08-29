<template>
    <div class="mr-t-body">
        <div class="header-grey"> 
        </div>
        <div class="login">
            <div class="login-in">
                <div class="form-group login-form-item">
                    <label>
                        name:
                    </label> 
                    <div> 
                        <input type="text" v-model="user_name" placeholder="write you name" class=""/>
                    </div>
                </div>
                <div class="form-group login-form-item">
                    <label>
                        password:
                    </label> 
                    <div> 
                        <input type="password" v-model="user_pwd" placeholder="write you password"/>
                    </div>
                </div>
                <center class="error_msg" style="color:#ddd;">  
                    {{ error_msg }}
                </center>
                <center class="form-group">
                    <button class="btn-login btn-full" @click="login">sign in</button>
                </center>
                <router-link to="/home" id="to_home"></router-link>
            </div>
        </div>
        <center>
            <router-link to="/index">
                I just want to experience it ~
            </router-link>
        </center>
    </div>
</template>

<script>
import { Toast } from 'mint-ui'
export default {
    data () {
        return {
            user_name: '',
            user_pwd: '',
            error_msg: 'Each field is required',
            user: null
        }
    },
    methods: {
        login () {
            var can_login = false;
            const name = this.user_name.trim()
            const pwd = this.user_pwd.trim()

            can_login = this.yz_input(name, 'str')
            can_login = this.yz_input(pwd, 'str')

            if (can_login) {
                this.check_user(name, pwd)
            }
        },
        yz_input (value, instance) {
            if (!value) {
                this.show_msg('Please check the input !', 2000)
                return false
            }
            if (instance === 'str') {
                if (value.length <= 2) {
                    this.show_msg('The number of characters filled in should be greater than 2 !', 4000)
                    return false
                }
            }
            else if (instance === 'int') {
                if (isNaN(value)) {
                    this.show_msg('The number type input box should be filled with Numbers !', 3000)
                    return false
                }
            }
            return true
        },
        show_msg (msg, time) {
            this.error_msg = msg
            setTimeout(() => {
                this.error_msg = 'Each field is required';
            }, time)
        },
        check_user (name, pwd) {
            const url = this.$web_conf.USER_URL + '/login?user_name=' + name + '&user_pwd=' + pwd
            this.$axios.get(url).then(
                response => {
                    const ret = response.data
                    const data_code = ret.code
                    if (data_code === 2000) {
                        this.user = ret.user
                        this.get_token(ret.user.lucy)
                    }
                    else {
                        this.show_msg(ret.msg, 3000)
                    }
                }
            ).catch(
                error => {
                    console.info(error, error.data)
                }
            )
        },
        get_token (lucy) {
            const url = this.$web_conf.USER_URL + '/login'
            let data = this.$qs.stringify({
                'lucy': lucy
            })
            this.$axios({
                method: 'post',
                url: url,
                data: data
            }).then(
                response => {
                    const ret = response.data
                    if (ret.code === 2000) {
                        this.user['token'] = ret.token
                        this.set_user(this.user)
                        this.$pubsub.publish('login', (true, this.user))
                        setTimeout(() => {
                            const login_a = document.getElementById('to_home');
                            login_a.click();
                        }, 1000)
                    }
                    else {
                        this.show_msg(ret.msg, 3000)
                    }
                }
            ).catch(
                error => {
                    console.info(error, error.data)
                }
            )
        },
        set_user (user) {
            this.$sql.save_data(user, 'lucy')
        }
    }
}
</script>

<style>
.login {
    width: 100%;
    margin: 0 auto;
    margin-top: 120px;
}
.login-in {
    width: 36%;
    margin: 0 auto;
    padding-bottom: 2px;
    background-color: rgb(u, 87, 87);
}
.btn-login {
    margin-top: 12px;
    margin-bottom: 6px;
    padding: 6px 12px;
    border: 1px solid #aaaaaa;
    background: #cccccc;
    border-radius: 3px;
}
.btn-login:hover {
}

@media screen and (max-width: 1200px) {
    .login-in {
        width: 45%;
    }
}
@media screen and (max-width: 758px) {
    .login-in {
        width: 66%;
    }
}
@media screen and (max-width: 568px) {
    .login-in {
        width: 98%;
    }
}
    /*
        FILTER: progid:DXImageTransform.Microsoft.Gradient(gradientType=0,startColorStr= #006f9e,endColorStr= #61c2ee);
        background: -ms-linear-gradient(top, #006f9e, #61c2ee);
        background: -moz-linear-gradient(top, #006f9e, #61c2ee);
        background: -o-linear-gradient(top, #006f9e, #61c2ee);
        background: -webkit-linear-gradient(top, #006f9e, #61c2ee);
    */

</style>