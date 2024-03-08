def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my group name")
    new_list = app.groups.get_group_list()
    old_list.append("my group name")
    assert sorted(old_list) == sorted(new_list)


