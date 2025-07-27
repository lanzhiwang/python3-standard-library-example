#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2009 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software
# and its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# Doug Hellmann not be used in advertising or publicity
# pertaining to distribution of the software without specific,
# written prior permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS, IN NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
# THIS SOFTWARE.
#
""" """

# end_pymotw_header
import grp

name = "admin"
info = grp.getgrnam(name)
print("Name    :", info.gr_name)
print("GID     :", info.gr_gid)
print("Password:", info.gr_passwd)
print("Members :", ", ".join(info.gr_mem))
