#Kill a program in puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path => '/usr/bin:/bin',
  onlyif => 'pgrep killmenow',
}

