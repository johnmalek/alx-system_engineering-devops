file {'/tmp/school':
  mode    => 0744,
  owner   => 'www-data',
  group   => ''www-data',
  content => 'I love Puppet'
  ensure  => file,
  path    => '/tmp/school'
}
