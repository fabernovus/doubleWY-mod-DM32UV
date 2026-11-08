#!/usr/bin/env python3
"""doubleWY Mod v1.0.0 for Baofeng DM32UV — patcher and installer.

  python3 doublewy_patcher.py                    # guida interattiva: legge la radio, crea e installa la mod
                                                 # interactive guide: reads the radio, builds and installs the mod
  python3 doublewy_patcher.py --firmware FILE    # solo crea il file (backup memoria programma, 049 OEM o mod)
                                                 # only build the file (program-memory backup, OEM 049 or mod)

Contiene solo le modifiche della doubleWY Mod, non il firmware Baofeng: la mod
si genera dal firmware originale letto dalla tua radio.
Contains only the doubleWY Mod changes, not Baofeng's firmware: the mod is
built from the original firmware read from your radio.
Required Notice: Copyright (c) 2026 Antonio IU1WWY (doubleWY). PolyForm Noncommercial 1.0.0.
Not affiliated with or endorsed by Baofeng.
"""
import argparse
import base64
import binascii
import datetime
import hashlib
import io
import struct
import sys
import time
import zipfile
import zlib
from pathlib import Path

VERSION = '1.0.0'
MOD_SHA256 = '66fcfe2558d2c2e025472c26ee119c1aa01f5e45e290de121968487d7b587dc4'
MOD_SIZE = 999680
# Memoria programma (GD25Q08, 1 MB): l'applicazione parte da 0xC000; il file di
# aggiornamento è un'intestazione di formato + l'applicazione.
# Program memory (1 MB): the application starts at 0xC000.
PROGMEM_SIZE, APP_OFFSET = 1 << 20, 0xC000
UPDATE_HEADER = b'BFUV32-V2'+b'\xff'*244+b'END'
# Basi riconosciute (049 originale e mod pubblicate) con la patch verso questa versione.
# Known bases (original 049 and published mods) with the patch to this version.
BASES = (
    ('OEM DM32.NRF.01.049', 873964, 'aff6b4dc09dcce45847173defba26e94157cc628af86826e21e5af227bdc52dd', (
        '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',
        'BbQw7wjTJvPgaYPGCxmD4oV38II5R6uU3kQIlpQc7dCg+J4MeIvgKuHccK1wnTnagMynK0ezvmGQ',
        'uW8Yo7zmDZHdEaTvnaUdkF7ZN4+/YbBhfXNYzMI3RV8ivolnfKQ7Iog+BZ9h/qNoiENIcRTuabhn',
        '4fqh6SAqnVKjYPtf49Sn8cz7K68ttRTPk/QxeJ7CcxueUDXVdjyRe+oZwdXby7U8SbJirVqSCcVa',
        'kyRtxdp+SdqLtWOSzC3WTkqyvFjzS3JbsXZekqXFWsKQ+No9xajGYi11SI58FCPJwyhGkseKtcOS',
        '7CvWeiV5qlg7NWRUOQvKWbVYS5Lk2WJtsyQvFWt9krSWaOckOa1Es/1JjvoSbbMkc0u0XZIsK9EO',
        'SrKmRDsiSV+J1ifJPSVavyQPIF9JHirRLGcFeRRFSLK3RMuR5IkSrVySp0u0dkluq9K6JbmrSjsm',
        'yf1V2klJdldp5yV5pEpL+LPMt0qrluSJKq1Jkv1V2n5Jouudl+SZKi31LVHz56sgFddrTW/JVl2v',
        '7Zekbb12WJJI0CtJ+3rtjCTz1mvsL4KsXK8lSdK9XrNLsnW9dvAvopjO9RjO67VjfxF9twveHrhj',
        '67V+mbhvvXZOkqfXa5ZzktP1mk2S76zXcsJkuSTN1do2SWK4tEsysVo7KElbtXZEkvZqrU+SedVa',
        'vyQrq7Vzeg7VmuWvkvdqzSbJzmot568Gk92S7KrWjkmyp1rzS/J4tXZekieqtYS3ZStUa6mS3LZF',
        'y5Pkri1atSQ7t2j7Jdm1ReuVZM8W7ZQkj23RzoBcQDxsgX7yaYxYPBe+H6eeqYZIwtMPfzWerR6I',
        'JTw7PVrq32Sn9Gg5kjzk0UolecyjVf9Nand456SHz0W7/iZnHHjPUvaYtp82WVWZpE++7Pdo/ZI8',
        '59HOSZJt1azvyJ60VVsoyWlbtXaQ2aSebxVKGKkXTdCx95P++IEoJRdxpXCVcJvhfHBnyTSaqvW9',
        'IwQcWU6kF++iJKE40tkG3hEW7H4EHUQQqXNdA3FqN/xH4J6GO4Hwk3ienqZZ/y4+D7aW2o+gS4g6',
        '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',
    )),
)
# Programma di lettura doubleWY (256 byte) caricato nella RAM dalla boot ROM.
# doubleWY reader stub (256 bytes) loaded into RAM by the boot ROM.
READER_STUB = bytes.fromhex('84ea2100443000e02f00573000e02c00593000e02900313000e0260000e02b0052314264fc0b00350436a84500e02300406d002e26e9fbff86ea1400b85d003600370085e05f00e00f000025002681ea10005a64f70b1f6c00e00600084f00e00300dd073f9421e4022001e9fdff00b43c78259421e4012001e9fdff009400e4ff203c7800000314000000030001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
READER_BASE = 0x00010000

TEXT = {
    'it': dict(
        title=f'doubleWY Mod v{VERSION} per Baofeng DM32UV',
        intro='Questa guida legge il firmware dalla radio, crea la mod e la installa.\n'
              'Servono: radio con batteria carica, cavo di programmazione USB, nessun altro\n'
              'programma che usi il cavo (CPS, browser con grid.radio).',
        no_serial='Manca il modulo pyserial. Installalo con:\n  {pip}\ne rilancia lo script.',
        ports='Porte seriali trovate:', no_ports='Nessuna porta seriale trovata. Collega il cavo e riprova.',
        choose_port='Numero della porta da usare [{default}]: ',
        read_title='PASSO 1/3 — Lettura della radio',
        read_steps='1. Spegni la radio e lascia il cavo collegato.\n'
                   '2. Premi Invio, poi ACCENDI la radio normalmente (senza tasti).\n'
                   '   Lo schermo resterà spento durante la lettura: è normale.',
        enter='Premi Invio per continuare... ',
        waiting='In attesa della radio (accendila ora)...', handshake='Radio collegata, avvio lettura.',
        no_handshake='La radio non ha risposto entro 2 minuti. Spegnila, controlla cavo e porta, e riprova:\n'
                     'va accesa DOPO aver premuto Invio.',
        no_stub='La radio ha risposto ma il caricamento del lettore non è riuscito. Spegnila e riprova.',
        reading='Lettura', saved='Backup salvato in: {path}\nCONSERVALO: contiene il firmware della tua radio.',
        detected='Firmware rilevato: {label}', up_to_date=f'La radio ha già la doubleWY Mod v{VERSION}.',
        reinstall='Vuoi reinstallarla comunque? [s/N] ',
        unknown='Firmware non riconosciuto: la mod non può essere applicata.\n'
                'Serve il firmware originale DM32.NRF.01.049 o una versione pubblicata della mod.',
        built='Mod creata: {path}', write_title='PASSO 2/3 — Modalità aggiornamento',
        write_steps='1. Spegni la radio (dopo la lettura è ferma) e lascia il cavo collegato.\n'
                    '2. Tieni premuti SK1 (tasto laterale) e PTT e accendi la radio:\n'
                    '   il LED diventa verde. Poi rilascia i tasti.',
        confirm='Installare doubleWY Mod v{version} sulla radio? [s/N] ',
        cancelled='Installazione annullata. Il file resta disponibile.',
        flash_title='PASSO 3/3 — Installazione',
        not_update_mode='La radio non è in modalità aggiornamento (SK1+PTT, LED verde). Nessuna modifica è stata fatta.',
        erasing='Cancellazione della memoria (circa 15 secondi)...', writing='Scrittura',
        done=f'Fatto! Spegni e riaccendi la radio: vedrai lo splash doubleWY e in Menu > Mod Info la versione {VERSION}.',
        failed='ERRORE durante la scrittura: {err}\nLa radio non ha un firmware completo, ma il bootloader è intatto:\n'
               'rimetti la radio in modalità aggiornamento (SK1+PTT) e lancia:\n  {cmd}',
        yes='s'),
    'en': dict(
        title=f'doubleWY Mod v{VERSION} for Baofeng DM32UV',
        intro='This guide reads the firmware from the radio, builds the mod and installs it.\n'
              'You need: a charged radio, the USB programming cable, and no other program\n'
              'using the cable (CPS, browser with grid.radio).',
        no_serial='The pyserial module is missing. Install it with:\n  {pip}\nthen run the script again.',
        ports='Serial ports found:', no_ports='No serial port found. Connect the cable and try again.',
        choose_port='Port number to use [{default}]: ',
        read_title='STEP 1/3 — Reading the radio',
        read_steps='1. Turn the radio off and keep the cable connected.\n'
                   '2. Press Enter, then TURN the radio ON normally (no keys).\n'
                   '   The screen stays off while reading: this is normal.',
        enter='Press Enter to continue... ',
        waiting='Waiting for the radio (turn it on now)...', handshake='Radio connected, reading.',
        no_handshake='The radio did not answer within 2 minutes. Turn it off, check cable and port, and try again:\n'
                     'turn it on AFTER pressing Enter.',
        no_stub='The radio answered but loading the reader failed. Turn it off and try again.',
        reading='Reading', saved="Backup saved to: {path}\nKEEP IT: it holds your radio's firmware.",
        detected='Detected firmware: {label}', up_to_date=f'The radio already has doubleWY Mod v{VERSION}.',
        reinstall='Reinstall it anyway? [y/N] ',
        unknown='Firmware not recognised: the mod cannot be applied.\n'
                'The original DM32.NRF.01.049 or a published mod version is required.',
        built='Mod built: {path}', write_title='STEP 2/3 — Update mode',
        write_steps='1. Turn the radio off (it is halted after reading) and keep the cable connected.\n'
                    '2. Hold SK1 (side key) and PTT and turn the radio on:\n'
                    '   the LED turns green. Then release the keys.',
        confirm='Install doubleWY Mod v{version} on the radio? [y/N] ',
        cancelled='Installation cancelled. The file is still available.',
        flash_title='STEP 3/3 — Installing',
        not_update_mode='The radio is not in update mode (SK1+PTT, green LED). Nothing was changed.',
        erasing='Erasing memory (about 15 seconds)...', writing='Writing',
        done=f'Done! Turn the radio off and on: you will see the doubleWY splash, and Menu > Mod Info shows {VERSION}.',
        failed='ERROR while writing: {err}\nThe radio has no complete firmware, but the bootloader is intact:\n'
               'put the radio in update mode again (SK1+PTT) and run:\n  {cmd}',
        yes='y'),
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def identify(data):
    """(label, image) for a raw image, a program-memory backup or a .zip, else None.
    The current version is reported with label None."""
    known = [(label, size, digest) for label, size, digest, _ in BASES]+[(None, MOD_SIZE, MOD_SHA256)]
    candidates = [data]
    if len(data) == PROGMEM_SIZE:
        candidates = [UPDATE_HEADER+data[APP_OFFSET:APP_OFFSET+size-256] for _, size, _ in known]
    elif data[:2] == b'PK':
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            sizes = {size for _, size, _ in known}
            candidates = [z.read(i) for i in z.infolist() if i.file_size in sizes]
    for image in candidates:
        for label, size, digest in known:
            if len(image) == size and sha256(image) == digest:
                return label, image
    return None


def apply(base, patch):
    blob = zlib.decompress(base64.b64decode(''.join(patch)))
    magic, size, count = struct.unpack_from('<4sII', blob)
    if magic != b'DWY1' or size != MOD_SIZE:
        raise ValueError('patch data corrupted')
    out = bytearray(base[:size])+bytes(max(0, size-len(base)))
    pos = 12
    for _ in range(count):
        offset, length = struct.unpack_from('<II', blob, pos); pos += 8
        out[offset:offset+length] = blob[pos:pos+length]; pos += length
    out = bytes(out)
    if sha256(out) != MOD_SHA256:
        raise ValueError('result verification failed')
    return out


def mod_from(found):
    """The mod image for an identified input (the input itself if already current)."""
    label, image = found
    return image if label is None else apply(image, next(p for l, _, _, p in BASES if l == label))


def progress(name, done, total, start):
    rate = done/max(time.time()-start, 1e-3)
    left = (total-done)/rate if rate else 0
    bar = '#'*int(30*done/total)
    sys.stdout.write(f'\r  {name} [{bar:<30}] {100*done//total:3d}%  {done//1024:4d}/{total//1024} KB  ~{left:3.0f} s ')
    sys.stdout.flush()
    if done == total:
        print()


class Radio:
    """Boot-ROM reader (doubleWY stub) and OEM bootloader writer over the programming cable."""
    ACK = b'\x02\x05\x00\x03'

    def __init__(self, serial_module, port):
        self.port = serial_module.Serial(port, 115200, timeout=0.5)

    def expect(self, n, value, timeout=0.5):
        self.port.timeout = timeout
        return self.port.read(n) == value

    def read_program_memory(self, t, wait=120):
        port = self.port
        print(t['waiting'])
        # The boot ROM announces itself only briefly at power-on: answer at once.
        buf, start = b'', time.time()
        port.timeout = 0.01
        port.reset_input_buffer()
        while buf[-4:] != b'\x02\x24\x00\x03':
            buf = (buf+port.read(1))[-4:]
            if time.time()-start > wait:
                raise SystemExit(t['no_handshake'])
        port.write(b'\x02\x14\x00\x03')
        time.sleep(0.05)
        port.reset_input_buffer()
        for k in range(0, len(READER_STUB), 256):
            payload = (READER_BASE+k).to_bytes(4, 'big')+b'\x00\x00\x00\x40'+READER_STUB[k:k+256]
            port.write(b'\x02\x18'+bytes([sum(payload) & 0xff])+b'\x03'+payload)
            if not self.expect(4, self.ACK, 1):
                raise SystemExit(t['no_stub'])
        entry = READER_BASE.to_bytes(4, 'big')
        port.write(b'\x02\x1B'+bytes([sum(entry) & 0xff])+b'\x03'+entry)
        if not (self.expect(4, self.ACK, 1) and self.expect(4, b'DWY1', 2)):
            raise SystemExit(t['no_stub'])
        print(t['handshake'])
        port.timeout = 2
        data, start = bytearray(), time.time()
        for offset in range(0, PROGMEM_SIZE, 256):
            for _ in range(3):
                port.reset_input_buffer()
                port.write(b'R'+offset.to_bytes(4, 'big'))
                block = port.read(258)
                if len(block) == 258 and int.from_bytes(block[256:], 'little') == sum(block[:256]) & 0xffff:
                    break
            else:
                raise SystemExit(f'read error at {offset:#x}')
            data += block[:256]
            if offset % 0x4000 == 0 or offset+256 == PROGMEM_SIZE:
                progress(t['reading'], offset+256, PROGMEM_SIZE, start)
        return bytes(data)

    def write_firmware(self, image, t):
        """OEM bootloader protocol, as the Baofeng CPS: nothing is erased before the info block."""
        port, payload = self.port, image[0x100:]
        if len(payload) % 1024 or len(payload) > 0xf4002:
            raise SystemExit('invalid firmware size')
        port.reset_input_buffer()
        for send, reply in ((b'\x52', b'\x06'), (b'\x4D\x00\x00\x00\x01', b'\x4D\x01\x09'), (b'\x06', b'BFUV32-V2'),
                            (b'\x45\x00\x00\x00\x00', b'\x06'), (b'\x31', b'\x43'), (b'\x01', b'\x43')):
            port.write(send)
            if not self.expect(len(reply), reply):
                raise SystemExit(t['not_update_mode'])
        info = b'doubleWY\x00'+str(len(payload)).encode()
        info += bytes(128-len(info))
        print(t['erasing'])
        port.write(b'\x00\xFF'+info+binascii.crc_hqx(info, 0).to_bytes(2, 'big'))
        if not self.expect(2, b'\x06\x43', 30):
            raise SystemExit(t['not_update_mode'])
        start, blocks = time.time(), len(payload)//1024
        for n in range(blocks):
            block = payload[n*1024:(n+1)*1024]
            port.write(b'\x02')
            if not self.expect(1, b'\x43'):
                raise IOError(f'block {n}')
            index = (n+1) & 0xff
            port.write(bytes([index, 0xff-index])+block+binascii.crc_hqx(block, 0).to_bytes(2, 'big'))
            if not self.expect(1, b'\x06', 5):
                raise IOError(f'block {n}')
            if n % 16 == 0 or n == blocks-1:
                progress(t['writing'], (n+1)*1024, blocks*1024, start)
        port.write(b'\x04')


def ask(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        return ''


def open_serial(t):
    pip = 'py -m pip install pyserial' if sys.platform.startswith('win') else 'python3 -m pip install pyserial'
    try:
        import serial
        from serial.tools import list_ports
    except ImportError:
        raise SystemExit(t['no_serial'].format(pip=pip))
    ports = sorted(list_ports.comports(), key=lambda p: p.device)
    ports = [p for p in ports if p.vid is not None] or ports  # USB adapters first; built-in UARTs only as fallback
    if not ports:
        raise SystemExit(t['no_ports'])
    print(t['ports'])
    default = next((i for i, p in enumerate(ports) if p.vid == 0x1a86), 0)
    for i, p in enumerate(ports, 1):
        print(f'  [{i}] {p.device}  {p.description or ""}')
    choice = ask(t['choose_port'].format(default=default+1))
    index = int(choice)-1 if choice.isdigit() and 0 < int(choice) <= len(ports) else default
    return Radio(serial, ports[index].device)


def install(radio, mod, t, retry):
    print(f"\n{t['write_title']}\n{t['write_steps']}")
    if ask(t['confirm'].format(version=VERSION)).lower() != t['yes']:
        print(t['cancelled'])
        return 0
    print(f"\n{t['flash_title']}")
    try:
        radio.write_firmware(mod, t)
    except (IOError, OSError) as error:
        print(t['failed'].format(err=error, cmd=retry))
        return 1
    print('\n'+t['done'])
    return 0


def interactive(output, t):
    print(f"\n{t['title']}\n{'='*len(t['title'])}\n{t['intro']}\n")
    radio = open_serial(t)
    print(f"\n{t['read_title']}\n{t['read_steps']}")
    ask(t['enter'])
    dump = radio.read_program_memory(t)
    backup = output/f"DM32UV-program-memory-{datetime.datetime.now():%Y%m%d-%H%M%S}.bin"
    backup.write_bytes(dump)
    print(t['saved'].format(path=backup))
    found = identify(dump)
    if found is None:
        print(t['unknown'])
        return 1
    print(t['detected'].format(label=found[0] or f'doubleWY Mod v{VERSION}'))
    if found[0] is None:
        print(t['up_to_date'])
        if ask(t['reinstall']).lower() != t['yes']:
            return 0
    mod = mod_from(found)
    target = output/f'doubleWY-mod-DM32UV-v{VERSION}.bin'
    target.write_bytes(mod)
    print(t['built'].format(path=target))
    return install(radio, mod, t, f'python3 doublewy_patcher.py --firmware "{backup}" --flash')


def main():
    parser = argparse.ArgumentParser(description=f'doubleWY Mod v{VERSION} for Baofeng DM32UV')
    parser.add_argument('--firmware', type=Path, help='program-memory backup (1 MB), OEM 049 or doubleWY Mod .bin/.zip')
    parser.add_argument('--output', type=Path, default=Path('.'), help='output folder')
    parser.add_argument('--flash', action='store_true', help='with --firmware: also install it (radio in update mode)')
    parser.add_argument('--lang', choices=('it', 'en'), help='language / lingua')
    args = parser.parse_args()
    lang = args.lang or ('en' if not args.firmware and ask('Lingua / Language: [1] Italiano  [2] English  [1]: ') == '2' else 'it')
    t = TEXT[lang]
    if not args.firmware:
        return interactive(args.output, t)
    found = identify(args.firmware.read_bytes())
    if found is None:
        print(f'{args.firmware}: firmware non riconosciuto / firmware not recognised')
        return 1
    print(f'Rilevato / Detected: {found[0] or "doubleWY Mod v"+VERSION} -> doubleWY Mod v{VERSION}')
    mod = mod_from(found)
    if found[0] is not None:
        target = args.output/f'doubleWY-mod-DM32UV-v{VERSION}.bin'
        if target.exists():
            print(f'{target} esiste già / already exists')
            return 1
        target.write_bytes(mod)
        print(f'OK: {target}\nSHA-256 {MOD_SHA256}')
    elif not args.flash:
        print(f'Già doubleWY Mod v{VERSION}: niente da fare. / Already doubleWY Mod v{VERSION}: nothing to do.')
        return 0
    if args.flash:
        return install(open_serial(t), mod, t, f'python3 doublewy_patcher.py --firmware "{args.firmware}" --flash')
    return 0


if __name__ == '__main__':
    sys.exit(main())
