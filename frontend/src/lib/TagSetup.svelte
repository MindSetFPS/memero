<script>
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher()

    export let value = []
    let currentTag = ''
    function addTag(){
        value = [...value, currentTag]
        currentTag=''
        dispatch('tag')
        console.log(value)
    }

</script>

<div>
    Tags
    <input type="text" name="tag" id="tags" bind:value={currentTag} />
    <button on:click|preventDefault={addTag} > Add </button>
    {#each value as tag}
        <div class="">
            {tag}
        </div>
    {/each}
</div>