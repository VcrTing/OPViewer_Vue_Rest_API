<template>
    <div class="img-list">
        <div class="img-list-header">
        </div>
        <ul class="img-list-ul">
            <li v-for="(img, index) in img_list" :key="img.id">
                <div class="img-every">
                    <div class="cover" @click="open_img_modal(index)">
                        <div :style="show_img(img.img_url)">
                        </div>
                    </div>
                    <div class="img-list-opt">
                        <button class="btn btn-full" @click="del_img(img.id, index)">delete</button>
                    </div>
                </div>
            </li>
        </ul>
        <div class="img-modal" v-if="show_img_modal">
            <div class="modal-header"> 
                <div class="close-modal" @click="close_modal()">&times;</div>
            </div>
            <iframe :src="this_img_url">

            </iframe>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        is_refresh: Boolean
    },
    data () {
        return {
            user: {},
            token: null,
            img_list: [],
            img_next_url: '',
            img_prev_url: '',
            this_img_url: null,
            show_img_modal: false
        }
    },
    mounted () {
        this.get_user()
        try{
            this.token = this.user.token
            const url = this.$web_conf.KUUKANN_URL + '/logic_img?lucy=' + this.user.lucy + '&token=' + this.token
            this.img_next_url = url
            this.get_img()
            
            window.addEventListener('scroll', this.handleScroll, true)
        }catch (e) {
            this.user = {
                'lucy': null,
                'token': null
            }
        }
    },
    watch: {
        is_refresh: {
            hanlder: function(new_val, old_val) {
                alert(this.is_refresh)
                if (new_val === true){
                    this.get_img()
                    
                }
            }
        }
    },
    methods: {
        handleScroll(e){
            var scrollTop = document.documentElement.scrollTop|| document.body.scrollTop;
            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
            var scrollHeight = document.documentElement.scrollHeight|| document.body.scrollHeight;
            if(scrollTop+windowHeight == scrollHeight) {
                this.get_scroll_img()
            }  
        },
        close_modal () {
            this.show_img_modal = false
        },
        open_img_modal (index) {
            this.show_img_modal = true
            this.this_img_url = this.$web_conf.KUUKANN_URL + '/util_img/' + this.img_list[index].id + '?flag=show&token=' + this.token + '&original_img=' + this.img_list[index].original_img_url
        },
        show_img (img_url) {
            const bg_img = 'background: url("' + img_url + '"); background-position: center center; background-size: cover;';
            return bg_img
        },
        get_img () {
            this.$axios.get(this.img_next_url).then(
                response => {
                    const ret = response.data
                    this.img_next_url = ret.next
                    this.img_prev_url = ret.previous
                    var img_list = ret.results.map(img => ({
                        'id': img.id,
                        'img_url': this.$web_conf.WEB_URL + img.comped_img,
                        'original_img_url': this.$web_conf.WEB_URL + img.original_img,
                        'create_time': img.create_time
                    }))
                    this.img_list = img_list
                }
            ).catch(
                error => {

                }
            )
        },
        get_scroll_img () {
            this.$axios.get(this.img_next_url).then(
                response => {
                    const ret = response.data
                    this.img_next_url = ret.next
                    this.img_prev_url = ret.previous
                    var img_list = ret.results.map(img => ({
                        'id': img.id,
                        'img_url': this.$web_conf.WEB_URL + img.comped_img,
                        'original_img_url': this.$web_conf.WEB_URL + img.original_img,
                        'create_time': img.create_time
                    }))
                    img_list.forEach(function(v) {this.img_list.push(v)}, this); 
                }
            ).catch(
                error => {

                }
            )
        },
        get_user () {
            const user = this.$sql.read_data('lucy')
            this.user = user
        },
        del_img (lucy, index) {
            if (window.confirm('You will delete this picture !')) {
                const url = this.$web_conf.KUUKANN_URL + '/opt_img/' + lucy
                const data = this.$qs.stringify({
                    'lucy': lucy,
                    'token': this.token
                })
                this.$axios({
                    url: url,
                    method: 'delete',
                    data: data
                }).then(
                    response => {
                        this.del_item(index)
                        alert('Delete success~')
                    }
                ).catch(
                    error => {
                        alert('Delete failed !!!')
                    }
                )
            }
        },
        del_item (index) {
            this.img_list.splice(index, 1)
        }
    }
}
</script>

<style>
.img-modal {
    background: rgba(0, 0, 0, 0.9);
    position: fixed;
    z-index: 6000;
    width: 100%;
    top: 0;
    left: 0;
    height: 100%;
}
.img-modal iframe {
    width: 100%;
    height: 100%;
    border: none;
}
.modal-header {
    position: fixed;
    height: 36px;
    width: 100%;
    font-size: 30px;
    color: #ffffff;
}
.img-list-ul {
    padding: 0 0 0 0;
}
.img-list-ul li{
    padding: 0 0;
    width: 20%;
    float: left;
    z-index: 100;
    margin-top: 6px;
    margin-bottom: 12px;
}
.img-every{
    position: relative;
    display: block;
}
.cover {
    width: 100%;
    height: 196px;
    border: 1px solid #aaaaaa;
    margin-left: -1px;
    overflow: hidden;
}
.cover:hover {
    border: 1px solid #00a8f3;
}
.cover div {
    z-index: 300;
    width: 100%;
    height: 100%;
    transition: all 0.5s;
}
.cover div:hover {
    transform: scale(1.03);
}

.img-list-opt button {
    padding: 2px 6px;
    font-size: 12px;
    margin-left: -1px;
    margin-top: -1px;
    color: rgba(101, 101, 101, 1);
    border: 1px solid rgba(64, 64, 64, 1);
    background-color: rgba(64, 64, 64, 1);
}
.img-list-opt button:hover {
    color: #00a8f3;
    border: 1px solid #00a8f3;
}

@media screen and (max-width: 1202px){
    .img-list-ul li{
        width: 20%;
    }
    .cover {
        height: 168px;
    } 
}
@media screen and (max-width: 1082px){
    .img-list-ul li{
        width: 20%;
    }
    .cover {
        height: 156px;
    } 
}
@media screen and (max-width: 762px){
    .img-list-ul li{
        width: 20%;
    }
    .cover {
        height: 126px;
    } 
}
@media screen and (max-width: 620px){
    .img-list-ul li{
        width: 25%;
    }
    .cover {
        height: 112px;
    } 
}
@media screen and (max-width: 492px){
    .img-list-ul li{
        width: 25%;
    }
    .cover {
        height: 100px;
    } 
}
</style>
