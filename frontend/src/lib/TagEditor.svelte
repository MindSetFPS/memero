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
            let cleanArray = []

            // remove whitespace at the end and begining of each tag
            toArray.forEach( word => {
                let cleanWord = word.trim()
                // check if word is empty
                if(word.length == 0){
                    return
                }
                // check if strng if made of just white spaces
                if (!word.replace(/\s/g, '').length) {
                    return
                }
                cleanArray.push(cleanWord)
            });
            
            let cleanArraytoString = cleanArray.toString()

            // remove annoying comma at the end
            let conditionalSum = $memesStore[memeIndex].tags.length > 0 ? ',' + $memesStore[memeIndex].tags : ''
            memesCopy[memeIndex].tags = cleanArraytoString  + conditionalSum

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
        }
    }
</script>