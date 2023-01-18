{#if filteredSearch.length == 0 || matchingElements.length > 0}
<div class="max-w-md" >
    <img src="{baseUrl}/image/{post.filename}" alt="" on:click={bigPicture}>
    <div>
        <p class="whitespace-nowrap overflow-hidden overflow-ellipsis">
            {post.filename}
        </p>
        <TagList tags={$memesStore[index].tags} on:deleteTag={handleTagDeleted} />
    </div>
    {#if isBigPicture }
        <div class="fixed h-screen w-screen top-0 left-0 z-20" >
            <div 
                class="
                    absolute z-20 top-0 
                    bg-white
                    h-1/2 w-1/2
                    left-1/2 -translate-x-1/2 translate-y-1/2
                    p-2 rounded-lg
                    text-center
                    lg:flex
                    lg:justify-start
                    scale-125
            ">
                <!-- <div>                   left-0  </div> -->
                <div 
                    class="h-full w-1/3 bg-contain bg-center bg-no-repeat " 
                    style="background-image: url({baseUrl}/image/{post.filename})"
                >
                </div>
                <div class="flex flex-col justify-center font-bold w-full h-full p-2">
                    <div class="flex w-full align-middle items-center my-2">
                        <div class="text-lg inline whitespace-nowrap">
                            Agregar tags
                        </div>
                        <TagEditor id={post.id} index={index} />
                    </div>
                    <div class="overflow-auto" >
                        <TagList tags={$memesStore[index].tags} on:deleteTag={handleTagDeleted} />
                    </div>
                    {#if showconfirmDelete}
                        De verdad quieres borrar este meme? Esto no se puede deshacer
                        <DeleteButton id={post.id} on:delete={deleteMeme} />
                    {:else}
                        <Button on:clicked={ () => showconfirmDelete = !showconfirmDelete} type="red" text="Borrar meme"   />
                    {/if}
                </div>
            </div>
            <GrayBackground on:clicked={bigPicture} />
        </div>
    {/if}
</div>
{/if}

<script>
    import { createEventDispatcher } from "svelte"
    import GrayBackground from "./GrayBackground.svelte";
    import Button from "./Button.svelte";
    import DeleteButton from "./DeleteButton.svelte";
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import TagEditor from "./TagEditor.svelte";
    import { memesStore } from "./store";

    export let post;
    export let index;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    let showconfirmDelete = false;
    const dispatch = createEventDispatcher()

    let baseUrl = getBaseUrl()
    $: {
        matchingElements = filteredSearch.filter(element => post.tags.includes(element))
    }

    function bigPicture(){
        isBigPicture = !isBigPicture
        showconfirmDelete = false
    }

    async function deleteMeme(event){
        const res = await fetch(`${baseUrl}/image/delete/${event.detail.id}`);
		const text = await res.json();
    
		if (res.ok) {
            dispatch('meme_deleted', {
                index: index
            })
            isBigPicture = !isBigPicture
		} else {
      throw new Error(text);
		}
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