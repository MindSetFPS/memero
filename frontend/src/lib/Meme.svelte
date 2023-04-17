<script>
    import { createEventDispatcher } from "svelte"
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import { memesStore } from "./store";
    import MemeDetails from "./MemeDetails.svelte";
    import IntersectionObserver from "svelte-intersection-observer"

    export let post;
    export let index;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()
    let element;
    let isOnScreen;

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
<IntersectionObserver {element} threshold={0.1}
    on:observe={(e) => {
        console.log(e.detail.isIntersecting)
        isOnScreen = e.detail.isIntersecting
    }}
>
    <div class="w-80 h-80 p-2" bind:this={element} >
            {#if isOnScreen }
                <div>
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
            {:else}
                <div></div>
            {/if}
        </div>
        </IntersectionObserver>
{/if}
    