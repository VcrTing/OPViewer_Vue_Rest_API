<template>
    <div class="mr-t-body home">
        <div class="img-opt"> 
            <div class="img-opt-in">
            </div>
        </div>
        <div class="home-in">
            <img-list :user="user" :is_refresh="is_refresh"/>
        </div>
        <router-view>
        </router-view>
        <center>
            <div class="iframe-modal"> 
                <button @click="plus">Plus</button>
                <input type="file" ref="inp" style="display:none;" id="the_img" v-on:change="up"/>
            </div>
            <div class="footer">
                author VcrT, email vcrting@163.com.
            </div>
        </center>
    </div>
</template>

<script>
import ImgList from '@/views/kuukann/ImgList.vue'
export default {
    data() {
        return {
            user: {},
            token: null,
            new_img: null,
            plus_img_iframe_src: null,
            is_refresh: false,
            upload_url: null
        }
    },
    mounted () {
        this.get_user()
        try{
            this.token = this.user.token
            this.plus_img_iframe_src = this.$web_conf.KUUKANN_URL + '/util_img/' + this.user.lucy + '?flag=plus&token=' + this.token
            this.upload_url = this.$web_conf.KUUKANN_URL + '/logic_img'
        }catch (e) {
            this.user = {
                'lucy': null,
                'token': null
            }
        }
    },
    components: {
        ImgList
    },
    methods: {
        get_user () {
            const user = this.$sql.read_data('lucy')
            this.user = user
        },
        get_new_img () {
            alrt('beclick')
            setTimeout(() => {
                this.is_refresh = true
            }, 1000)
        },
        plus () {
            const the_img = document.getElementById('the_img')
            the_img.click()
        },
        up () {
            let i_dom = this.$refs.inp
            this.file = i_dom.files[0]
            
            var formdata = new FormData();
            formdata.append('new_img', this.file);
            formdata.append('lucy', this.user.lucy);
            formdata.append('token', this.token)

            this.$axios({
                url: this.upload_url + '?token=' + this.token,
                method: 'post',
                data: formdata,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(re => {
                alert('Plus picture success ~')
            })
            .catch(err => {
                console.log(err);
            })

        }
    }
}
</script>

<style>
.home {
    width: 100%;
    padding-top: 1px;
}
.home-in {
    width: 86%;
    margin: 0 auto;
}
.img-opt {
    z-index: 2000;
    border-radius: 1px;
    background-color: #eeeeee;
    color: rgba(101, 101, 101, 1);
    font-weight: inherit;
    height: 18px;
    position: fixed;
    width: 100%;
    right: 0;
}
.iframe-modal {
    position: fixed;
    bottom: 0;
    right: 0;
    z-index: 5000;
    background: rgba(88, 88, 88, 1);
    overflow-y: hidden;
}
.iframe-modal:hover {
    background: rgba(101, 101, 101, 1);
}
.iframe-modal button {
    width: 60px;
    height: 40px;
    padding: 0 0;
    border: none;
    background: rgba(255, 255, 255, 0.5)
}

.img-opt-item {
    display: inline-block;
    height: 20px;
    padding: 0 12px;
    font-size: 12px;
}
.img-opt-item:hover {
    background-color: rgba(219, 219, 219, 1);
    cursor: pointer;
}

@media screen and (max-width: 1202px){
    .home-in {
        width: 88%;
    } 
}
@media screen and (max-width: 1082px){
    .home-in {
        width: 92%;
    } 
}
@media screen and (max-width: 762px){
    .home-in {
        width: 96%;
    } 
}
@media screen and (max-width: 492px){
    .home-in {
        width: 98%;
    } 
}

.footer {
    width: 100%;
    color: rgba(219, 219, 219, 1);
    margin-top: 18px;
    margin-bottom: 12px;
    float: left;
}
</style>
