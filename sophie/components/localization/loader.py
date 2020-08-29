# Copyright (C) 2018 - 2020 MrYacha.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

import os
from typing import Any, List

import yaml

from sophie.utils.logging import log

LANGUAGES: List[str] = []


def load_all_languages() -> None:
    from sophie.utils.loader import LOADED_MODULES

    for module in LOADED_MODULES.values():
        log.debug(f"Loading localizations from {module.name} module")

        path = module.path / "translations"
        if not path.exists():
            log.debug(f"No translations directory found for module {module.name}")
            continue

        for file_name in os.listdir(path):
            lang_name = file_name.split('.')[0]
            with open(f"{path}/{file_name}") as f:
                lang = yaml.load(f, Loader=yaml.SafeLoader)

                if not hasattr(module.base, 'translations'):
                    module.data['translations'] = {}

                if lang_name not in LANGUAGES:
                    LANGUAGES.append(lang_name)

                module.data['translations'][lang_name] = lang


def __setup__() -> Any:
    load_all_languages()
