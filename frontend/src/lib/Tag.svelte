<script>    
    import { createEventDispatcher } from "svelte"

    export let tag

    let dispatch = createEventDispatcher()

    function handleClick(){
        dispatch('delete', {
            tag: tag
        })
    }

</script>
<div 
class="
    hover:bg-orange-500 font-normal rounded-full bg-slate-400 inline-block 
    mx-1 px-2 my-1">
{tag}

<span
    on:click={handleClick} 
    class="hover:bg-black rounded-full text-xs" >🚽</span>
</div>