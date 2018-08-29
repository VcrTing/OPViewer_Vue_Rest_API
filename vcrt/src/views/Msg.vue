<template>
    <div class="mr-t-body msg">
        <center>
            <div class="msg-in">
                <h2 class="msg-header">
                    Guidelines and Information
                </h2>
                <div class="plant">
                    <div v-for="msg in msg_list" :key="msg.id" class="msg-every">
                        <div class="msg-content">
                            {{ msg.content }}
                        </div>
                    </div>
                </div>
                <div class="show_img"> 
                    <img :src="img_url"/>
                </div>
            </div>
                <p class="msg-header mr-t-big">
                    author VcrT, email vcrting@163.com
                </p>
        </center>
    </div>
</template>

<script>
export default {
    data () {
        return {
            msg_list: [
                {
                    'id': 1,
                    'content': 'Our platform is focused on the business of storing photos, and the photos stored by users are permanent.'
                },
                {
                    'id': 2,
                    'content': 'When using this platform, you should log in using your account, which is distributed by the administrator.'
                },
                {
                    'id': 3,
                    'content': 'Log in and enter the home screen, which has the plus button at the bottom right corner to add photos.'
                },
                {
                    'id': 4,
                    'content': 'The photos you added will be displayed in the home screen, with a delete button at the bottom of each photo to delete it.'
                },
                {
                    'id': 5,
                    'content': 'The platform will make corresponding amount of compression according to the width and height of the photo, which is to improve the users experience. Click the picture on the home interface to view the original image'
                }
            ],
            user: {
                'lucy': null,
                'token': null,
                'user_face': '../static/assets/Contact.png',
                'user_name': 'VcrT'
            },
            img_url: null
        }
    },
    mounted () {
        this.get_user()
        this.get_msg()
    },
    methods: {
        get_user () {
            const user = this.$sql.read_data('lucy')
            if (user) {
                this.user = user
            } 
        },
        get_msg () {
            this.$axios({
                url: this.$web_conf.KUUKANN_URL + '/opt_img/1?token=' + this.user.token,
                method: 'get'
            }).then(
                Response => {
                    const ret = Response.data
                    console.info(ret)
                    this.img_url = this.$web_conf.MEDIA_URL + ret.url
                }
            ).catch(
                error => {
                    alert('error')
                }
            )
        }
    }
}
</script>

<style>
.msg-in {
    min-height: 560px;
    padding-top: 1px;
    background-color: rgba(78, 78, 78, 0.6);
}
.show_img {
    width: 100%;
    height: auto;
    margin-top: 24px;
}
.show_img img {
    width: 100%;
    height: auto;
}
.msg-header {
    color: #ffffff;
}
.msg-every {
    padding: 0 12px;
    margin-top: 24px;
    color: #ffffff;
    text-shadow: 1px 0px 3px rgba(0, 0, 0, 0.5)
}
.msg-every:hover {
    color: rgba(255, 255, 255, 1);
    text-decoration: underline;
}
</style>
