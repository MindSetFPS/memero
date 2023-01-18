<div 
    class="shadow-lg rounded-xl p-2 fixed bottom-0 right-0 m-4 bg-white z-30" 
>
    {#if isBubble}
        <div on:click={ () => isBubble = !isBubble}
            on:keypress={() => isBubble = !isBubble} 
            class="text-4xl">
            Subir un meme 🤡
        </div>
    {:else}
        {#if isUploading}
            <div class="animate-pulse">
                Subiendo memes <span >🤡</span>
            </div>
        {/if}
        {#if !isUploading}
            <form
            action="/" 
            method="post" 
            enctype="multipart/form-data" 
            on:submit|preventDefault={handleUpload}
                class=""
            >
            <div>
                <input type="file" id="myFile" name="file" bind:files multiple >
            </div>
            <TagSetup bind:value={tags} on:tag={() => console.log(tags)} />
                <div>
                    <Button on:clicked={() => isBubble = true} type="green" text="Cerrar">
                        Cerrar
                    </Button>
                    <input type="submit" value="Upload" class="bg-blue-500 hover:bg-blue-600 text-white">
                </div>
            </form>
        {/if}
    {/if}
</div>

  <script>
    import TagSetup from "./TagSetup.svelte";
    import { createEventDispatcher } from "svelte"
    import Button from "./Button.svelte";
    import getBaseUrl from "./getBaseUrl";

    let files;
    let tags;
    let baseUrl = getBaseUrl()
    let isBubble = true
    let isUploading = false
   
    let dispatch = createEventDispatcher()

    async function handleUpload(event){
        const formData = new FormData()
        for (let i = 0; i < files.length; i++){
            console.log(files[i].name)
            formData.append('file', files[i])
        }

        formData.append('tags', tags)

        isUploading = true
        const res = await fetch(baseUrl + '/', {
            method: 'POST',
            body: formData
        })
        // const text = await res.json()

        if (res.ok) {
            dispatch('filesUploaded')
            event.target.reset()
            isUploading = false
        }
    }
</script>