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
    export let id;
    export let index;
    export let isBigPicture;
    let showconfirmDelete = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()

    function bigPicture(){
        if(isBigPicture){
            dispatch("exitBigPicture")
        }
        showconfirmDelete = false

        //copy the current list of memes
        let memesCopy = [...$memesStore]

        //sort by tag length
        memesCopy.sort( (meme1, meme2) => {
            let tags1 = meme1.tags.length
            let tags2 = meme2.tags.length
            
            if(tags1 < tags2){
                return 1
            }
            if(tags1 > tags2){
                return -1
            }
            return 0
        })
        //replace with the copy
        memesStore.update((value) =>  value = memesCopy)
    }

    async function deleteMeme(event){
        const res = await fetch(`${baseUrl}/image/delete/${event.detail.id}`);
		const text = await res.json();
    
		if (res.ok) {

            //copy the current list of memes
            const memeIndex = index
            console.log(memeIndex)
            let memesCopy = [...$memesStore]

            //edit the copy
            memesCopy.splice(memeIndex, 1)

            //replace with the copy
            memesStore.update((value) =>  value = memesCopy)
            isBigPicture = !isBigPicture
		} else {
      throw new Error(text);
		}
    }

    async function handleTagDeleted(event){

        const memeIndex = index
        //copy the current list of memes
        let memesCopy = [...$memesStore]

        //edit the copy
        memesCopy[memeIndex].tags = event.detail.taglist.toString()

        //replace with the copy
        memesStore.update((value) =>  value = memesCopy)


        //  edit in db
        const res = await fetch(`${baseUrl}/image/edit/${id}`, {
                method: "POST",
                body: JSON.stringify({
                    tags: memesCopy[memeIndex].tags
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            const text = await res.json();


    }
</script>

{#if isBigPicture }
<div class="h-full w-full fixed top-0 left-0 z-20 bg-pink-100/50"  >
    <div class="w-full h-full absolute flex flex-col justify-end z-30 bg-pink-50/50 "> 
        
        <div class="h-5/6 grid justify-center content-center " > 
            <img 
                src="{baseUrl}/image/file/{post.filename}" 
                class="max-h-full mx-auto" 
                alt=""
            >
        </div>

        <div class="h-1/6 w-full flex flex-col justify-center font-bold p-2 bg-white">
            {index}
            <div class="flex w-full align-middle items-center">
                <div class="text-lg inline whitespace-nowrap mx-2 ">
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
    <GrayBackground on:clicked={bigPicture}/>
</div>
{/if}