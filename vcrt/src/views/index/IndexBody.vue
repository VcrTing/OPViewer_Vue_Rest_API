<template>
    <div>
        <div class="index-body-in" id="index-body-in">
            <div class=""> 
                <index-pic/>
            </div>
        </div>
        <div class="index-footer"> 
            <index-footer/>
        </div>
    </div>
</template>

<script>
import IndexPic from './IndexPic.vue'
import IndexFooter from './IndexFooter.vue'
export default {
    components: {
        IndexPic,
        IndexFooter
    },
    mouted () {
        
    }
}

</script>

<style>
.index-body-in {
    margin: 0 auto;
    padding: 0 12px;
    border: 1px solid #ffffff;
}
.index-body-in:hover {
    border: 1px solid #00a8f3;
}
</style>
