<script>
    import { createEventDispatcher } from "svelte"
    import Tag from "./Tag.svelte";
    export let tags
    let taglist = tags.split(",")
    let dispatch = createEventDispatcher()

    function handleTagDeleted(event){
        const index = taglist.findIndex( (id) => id == event.detail.tag)
        dispatch('deleteTag', {
            tag: event.detail.tag,
            index: index
        })  
        // taglist.splice(index, 1)
        // taglist = taglist
    }
</script>

<div class="relative h-full w-full text-sm overflow-auto " >
    {#each taglist as tag}
        <Tag tag={tag} on:delete={handleTagDeleted} />
    {/each}
</div>
