$(document).ready(function () {
  function deleteUser(id) {
    $.ajax({
      url: '/users/delete/' + id,
      dataType: 'json',
      success: function (response) {
        console.log(response);
        updateUsers();
      },
      error: function (error) {
        console.log(error);
        updateUsers();
      }
    });
  }

  function updateUsers() {
    $.ajax({
      url: '/users/list',
      dataType: 'json',
      success: function (response) {
        var root = $('#users').html("");

        for (var id in response.users) {
          if (response.users.hasOwnProperty(id)) {
            var username = response.users[id];
            var htmlBlock = "<tr><td>" +
              username +
              "</td><td><button class='btn btn-danger btn-xs delete_button' data-user-id='" +
              id +
              "'>delete</button></td></tr>";
            root.append(htmlBlock);
          }
        }

        addDeleteCallbacks();
      },
      error: function (error) {
        console.log(error);
      }
    });
  }

  function showDiv() {
    document.getElementById('winners_div').style.display = 'block';
  }

  function chooseWinners() {
    $.ajax({
      url: '/users/winners',
      dataType: 'json',
      success: function (result) {
        showDiv();
        result = result['users'];
        $('#list1').html(result[0]);
        $('#list2').text(result[1]);
        $('#list3').text(result[2]);
      }
    });
  }

  function addUser(value) {
     $.ajax({
      type: 'POST',
      url: '/users/create',
      dataType: 'json',
      data: {username: value},
      success: function (response) {
       if (response.status == '200') {
        updateUsers();
        }
       else if (response.status == '422') {
        $('#error').html("Please enter a username");
       }
       else {
        $('#error').html("Current user is already registered");
       }
      },
      error: function (error) {
        console.log(error);
      }
    });
  }

  function addDeleteCallbacks() {
    $('.delete_button').click(function () {
    var id = $(this).attr('data-user-id');
    deleteUser(id);
  });
  }

  $('#choose_winners').click(function () {
    chooseWinners();
    updateUsers();
  });

  $('#add_user').click(function () {
    var value = $('#username').val();
    addUser(value);
    updateUsers();
  });

  updateUsers();


});
