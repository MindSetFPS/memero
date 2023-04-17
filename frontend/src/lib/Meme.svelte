<script>
    import { createEventDispatcher } from "svelte"
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import { memesStore } from "./store";
    import MemeDetails from "./MemeDetails.svelte";

    export let post;
    export let index;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()

    $: {
        matchingElements = filteredSearch.filter(element => post.tags.includes(element))
    }

    function handleTagDeleted(event){
        dispatch('deleteTag', {
            tag: event.detail.tag,
            index: index,
            memeId: post.id,
            taglist: event.detail.taglist
        })  
    }
        
</script>

{#if filteredSearch.length == 0 || matchingElements.length > 0}
    <div class="w-80 h-80 p-2" >
        <img class="object-cover h-56 w-80 hover:object-scale-down hover:mx-auto z-10 hover:z-100 transition" src="{baseUrl}/image/file/{post.filename}" alt="" on:click={ () => {
            isBigPicture = !isBigPicture
            console.log(isBigPicture)
            }}>
        <div class="h-24" >
            <p class="whitespace-nowrap overflow-hidden overflow-ellipsis">
                {post.filename}
            </p>
            <TagList tags={$memesStore[index].tags} on:deleteTag={handleTagDeleted} />
        </div>
        <MemeDetails 
            on:deleteTag={handleTagDeleted} 
            on:exitBigPicture={ () => isBigPicture = !isBigPicture} 
            index={index} 
            id={post.id}
            post={post}
            isBigPicture={isBigPicture}
        />
    </div>
{/if}
    