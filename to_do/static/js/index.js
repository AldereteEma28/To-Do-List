function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    function markComplete(id) {
    var isCompleted = document.getElementById(`checkbox-${id}`).checked;
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    fetch(`/mark-complete/${id}/`, {
        method: 'PUT',
        body: JSON.stringify({
            'task_completed': isCompleted,
        }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        }
    });
}