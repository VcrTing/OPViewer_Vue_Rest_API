<template>
    <div>
        <div class="index-pic"> 
            <div id="index-pic_01" >
                <img src="static/assets/index_01.jpg"/>
            </div> 
            <div id="index-pic_02" >
                <img src="static/assets/index_02.jpg"/>
            </div> 
            <div id="index-pic_03" >
                <img src="static/assets/index_03.jpg"/>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.index-pic {
    width: 40%;
    margin: 0 auto;
}
.index-pic div {
    width: 100%;
    float: left;
    border: 1px solid #00a8f3;

}
.index-pic div:hover {
    border: 1px solid #000000;
}
.index-pic div img {
    width: 100%;
    float: left;
}

#index-pic_01 {
    width: 65.5%;
}
#index-pic_02, #index-pic_03 {
    width: 32.78%;
}
#index-pic_01, #index-pic_02 {
    margin-top: 26px;
}
@media screen and (max-width: 1200px) {
    .index-pic {
        width: 66%;
        margin: 0 auto;
    }
}
@media screen and (max-width: 990px) {
    .index-pic {
        width: 80%;
        margin: 0 auto;
    }
}
@media screen and (max-width: 460px) {
    .index-pic {
        width: 88%;
        margin: 0 auto;
    }
}
@media screen and (max-width: 390px) {
    .index-pic {
        width: 98%;
        margin: 0 auto;
    }
}
</style>
