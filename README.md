# Nomad

![Molecule](https://github.com/DaazKu/ansible-nomad/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)
[![Galaxy](https://img.shields.io/badge/Galaxy-ansible__nomad-informational?logo=Ansible&logoColor=848c96)](https://galaxy.ansible.com/daazku/ansible_nomad)

This ansible role install Nomad and expect you to **supply your own configuration templates**.

See:
- [`nomad_config_template`](#nomad_config_template)
- [`nomad_extra_config_templates`](#nomad_extra_config_templates)

Nomad has MANY configuration parameters and trying to cover all of them with ansible variables makes things awfully complicated,
hard to maintain and frustrating when some options are not handled. You might also prefer to use HCL over the JSON format...
For these reasons, this role handles the installation of Nomad and use your supplied configuration templates so that everyone's life is made easier!

## Role Variables

### `nomad_bin_dir`
- Nomad binary directory
- Default value: `/usr/local/bin`

### `nomad_config_dir`
- Base configuration directory
- Default value: `/etc/nomad`

### `nomad_config_template`
- Path to the configuration template to use
    - **Must be supplied**
    - Resulting config will be the file name without the `.j2` extension. ie. `/some/path/config.hcl.j2` would result in `{{ nomad_config_dir }}/config.hcl`

### `nomad_data_dir`
- Nomad data directory
- Default value: `/var/lib/nomad'`

### `nomad_extra_config_dir`
- Extra configuration directory
- Default value: `{{ nomad_config_dir }}/nomad.d`

### `nomad_extra_config_templates`
- Extra configuration templates to render
    - Resulting configs will be the files name without the `.j2` extension. ie. `/some/path/my-extra-config.hcl.j2` would result in `{{ nomad_extra_config_dir }}/my-extra-config.hcl`
- Default value: `[]`

### `nomad_group`
- Nomad unix group
  - Note that for Nomad clients this should be changed to `root`. See: [Nomad User Permissions](https://www.nomadproject.io/docs/install/production/requirements#user-permissions)
- Default value: `nomad`

### `nomad_user`
- Nomad unix user
  - Note that for Noad clients this should be changed to `root`. See: [Nomad User Permissions](https://www.nomadproject.io/docs/install/production/requirements#user-permissions)
- Default value: `nomad`

### `nomad_version`
- Version to install
- Default value: 1.1.2
