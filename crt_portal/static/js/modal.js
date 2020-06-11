(function() {
  var previous_onkeydown = document.onkeydown;

  var modal = document.getElementById('intake_template');
  var notification = document.getElementById('response_copied_notification');

  function openModal() {
    notification.setAttribute('hidden', 'hidden');
    document.onkeydown = function(event) {
      event = event || window.event;
      var isEscape = false;
      if ('key' in event) {
        isEscape = event.key === 'Escape' || event.key === 'Esc';
      } else {
        isEscape = event.keyCode === 27;
      }
      if (isEscape) {
        closeModal();
      }
    };
    modal.removeAttribute('hidden');
    document.body.classList.add('is-modal');
  }

  function closeModal() {
    document.onkeydown = previous_onkeydown;
    modal.setAttribute('hidden', 'hidden');
    document.body.classList.remove('is-modal');
  }

  var contact = document.getElementById('contact_complainant');
  contact.onclick = function(event) {
    event.preventDefault();
    if (modal.getAttribute('hidden') !== null) {
      openModal();
    } else {
      closeModal();
    }
  };

  var cancel_modal = document.getElementById('intake_template_cancel');
  cancel_modal.onclick = function(event) {
    event.preventDefault();
    closeModal();
  };

  var copy = document.getElementById('intake_copy');
  var options = document.getElementById('intake_select');
  var letter = document.getElementById('intake_letter');
  var description = document.getElementById('intake_description');
  options.onchange = function(event) {
    event.preventDefault();
    var index = event.target.selectedIndex;
    var option = event.target.options[index];
    description.innerHTML = option.dataset['description'];
    letter.innerHTML = option.dataset['content'];
    if (index >= 1) {
      copy.removeAttribute('disabled');
    } else {
      copy.setAttribute('disabled', 'disabled');
    }
  };

  copy.onclick = function(event) {
    notification.removeAttribute('hidden');
    event.preventDefault();
    const el = document.createElement('textarea');
    el.value = letter.value;
    el.setAttribute('readonly', '');
    el.style.position = 'absolute';
    el.style.left = '-9999px';
    document.body.appendChild(el);
    el.select();
    el.setSelectionRange(0, 99999); // mobile
    document.execCommand('copy');
    document.body.removeChild(el);
    closeModal();
    notification.classList.add('fade-out');
    // hidden cannot be a CSS transition.
    window.setTimeout(function() {
      notification.setAttribute('hidden', 'hidden');
      notification.classList.remove('fade-out');
    }, 1000);
  };
})();