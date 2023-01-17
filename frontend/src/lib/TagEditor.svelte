    <input 
        class="w-full"
        type="text" 
        name="tag" 
        id="tag" 
        placeholder="agrega un nuevo tag" 
        on:keypress={addTag} 
        bind:value={value}
    >

<script>
    import { memesStore } from "./store";
    import getBaseUrl from "./getBaseUrl";
    export let id;
    export let index;
    let value;

    let baseUrl = getBaseUrl()

    async function addTag(event){
        if(event.keyCode == 13){

            //copy the current list of memes
            const memeIndex = index
            let memesCopy = [...$memesStore]

            //edit the copy

            let toArray = value.split(",")
            let toString_ = toArray.toString()

            memesCopy[memeIndex].tags = toString_  + ',' + $memesStore[memeIndex].tags
            // console.log(memesCopy[memeIndex].tags)

            //replace with the copy
            memesStore.update((value) =>  value = memesCopy)

            value = ''

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

            console.log(text)
        }
    }

    function handleTagDeleted(){

    }
</script>