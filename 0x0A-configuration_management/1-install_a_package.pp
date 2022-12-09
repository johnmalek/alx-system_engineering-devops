# Install flask from pip3 using puppet
file {'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
