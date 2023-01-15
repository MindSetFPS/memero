{#if filteredSearch.length == 0 || matchingElements.length > 0}
<div class="max-w-md">
    <img src="{baseUrl}/image/{post.filename}" alt="">
    <div>
        {post.filename}
        <Tag tags={post.tags} />
    </div>
</div>
{/if}

<script>
    import Tag from "./Tag.svelte";
    import getBaseUrl from "./getBaseUrl";
    export let post;
    export let filteredSearch;
    let matchingElements

    let baseUrl = getBaseUrl()
    $: {
        // console.log(filteredSearch)
        matchingElements = filteredSearch.filter(element => post.tags.includes(element))
        console.log(matchingElements)
    }
</script>